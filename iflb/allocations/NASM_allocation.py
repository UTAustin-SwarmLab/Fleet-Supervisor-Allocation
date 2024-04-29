from .base_allocation import Allocation
import numpy as np
import heapq


class NASMAllocation(Allocation):
    """
    An allocation strategy that prioritizes robots by submodular maximization
    """

    def allocate(self, allocation_metrics, network):
        """
        Allocate robots to environments based on submodular maximization using
        facility location objective function.
        """

        human_timers = allocation_metrics["human_timers"]

        assignment_matrix = allocation_metrics["assignments"].copy()

        for i in range(self.exp_cfg.num_humans):
            if human_timers[i] >= self.exp_cfg.min_int_time:
                assignment_matrix[:, i] = 0

        prev_allocations = assignment_matrix.sum(axis=1)

        weighted_similarity = (
            self.cfg.state_similarity_ratio * allocation_metrics["state_similarity"]
            + (1 - self.cfg.state_similarity_ratio)
            * allocation_metrics["action_similarity"]
        )

        uncertainty = allocation_metrics["uncertainty"]

        # Assign 0 uncertainty to environments that are lower than the uncertainty threshold
        uncertainty[uncertainty < self.cfg.uncertainty_thresh] = 0

        risk = allocation_metrics["risk"].reshape(-1)

        # Assign 0 risk to environments that are lower than the risk threshold
        risk[risk < self.cfg.risk_thresh] = 0

        total_informativeness = (
            self.cfg.uncertainty_ratio * uncertainty
            + (1 - self.cfg.uncertainty_ratio) * risk
        )

        M = (weighted_similarity * total_informativeness).T

        constraint_violation = allocation_metrics["constraint_violation"]

        constraint_M = np.eye(M.shape[0]) * constraint_violation

        # Before the warmup period, don't include constraint violation in the prioritization
        if self.cfg.warmup_penalty > allocation_metrics["time"]:
            M = M - self.cfg.constraint_alpha * constraint_M
        else:
            M = M + self.cfg.constraint_alpha * constraint_M

        # Based on current allocations find the max M values

        max_M = np.max(M * prev_allocations, axis=1).reshape(-1, 1)

        marginal_contrib = -(np.maximum(max_M, M).sum(axis=0) - max_M.sum())

        max_M = [max_M]
        probability = [1.0]

        marg_contr = [(marginal_contrib[i], i) for i in range(len(marginal_contrib))]

        heapq.heapify(marg_contr)

        env_priorities = list()

        # Marginalize Over all the possible allocations based on the current allocations
        # To find non-adaptive submodular maximization for the stochastic submodular maximization

        # If the marginal increase in the submodular objective is lower than a specific threshold stop the allocation

        marginal_increase_flag = False
        for j in range(self.exp_cfg.num_humans - int(prev_allocations.sum())):
            while 1:
                cur_el = heapq.heappop(marg_contr)
                cur_contr = 0
                for k in range(2 ** (j) - 1, 2 ** (j + 1) - 1):
                    cur_contr += (
                        -(
                            np.maximum(max_M[k], M[:, cur_el[1]].reshape(-1, 1)).sum()
                            - max_M[k].sum()
                        )
                        * probability[k]
                        * network.get_connection_probability(cur_el[1])
                    )
                if cur_contr <= marg_contr[0][0]:
                    if abs(cur_contr) < self.cfg.marginal_increase_threshold:
                        marginal_increase_flag = True
                        break

                    env_priorities.append(cur_el[1])

                    # Update the max_M values, and the probability of the allocation for successfull and unsuccessful allocations
                    for k in range(2 ** (j) - 1, 2 ** (j + 1) - 1):

                        # Successfull allocation
                        max_M.append(
                            np.maximum(max_M[k], M[:, cur_el[1]].reshape(-1, 1))
                        )
                        probability.append(
                            probability[k]
                            * network.get_connection_probability(cur_el[1])
                        )

                        # Unsuccessfull allocation
                        max_M.append(max_M[k])
                        probability.append(
                            probability[k]
                            * (1 - network.get_connection_probability(cur_el[1]))
                        )

                    break
                else:
                    heapq.heappush(marg_contr, (cur_contr, cur_el[1]))
            if marginal_increase_flag:
                break

        return env_priorities
