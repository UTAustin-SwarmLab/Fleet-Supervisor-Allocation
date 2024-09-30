from .base_allocation import Allocation
import numpy as np
import heapq


class ASAAllocation(Allocation):
    """
    An allocation strategy that prioritizes robots by adaptive submodular maximization
    """

    def allocate(
        self,
        allocation_metrics,
        network,
        successfull_allocations,
        failed_allocations,
        prev_allocations,
    ):
        """
        Allocate robots to environments based on submodular maximization using
        facility location objective function.
        """

        prev_allocations[successfull_allocations] = 1



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

        # Add prioritization for environments that are constraint violating

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

        marg_contr = [
            (marginal_contrib[i], i)
            for i in range(len(marginal_contrib))
            if i not in failed_allocations and i not in successfull_allocations and prev_allocations[i] == 0 
        ]

        heapq.heapify(marg_contr)

        # Find the adaptive submodular maximization for the stochastic submodular maximization

        # if the marginal increase in the submodular objective is lower than a specific threshold
        # stop the allocation

        while 1:
            cur_el = heapq.heappop(marg_contr)
            cur_contr = -(
                np.maximum(max_M, M[:, cur_el[1]].reshape(-1, 1)).sum() - max_M.sum()
            ) * self.network_connection_probabilities[cur_el[1]]

            if cur_contr <= marg_contr[0][0]:
                if abs(cur_contr) < self.cfg.marginal_increase_threshold:
                    env_priority = None
                else:
                    env_priority = cur_el[1]
                break
            else:
                heapq.heappush(marg_contr, (cur_contr, cur_el[1]))

        return env_priority
