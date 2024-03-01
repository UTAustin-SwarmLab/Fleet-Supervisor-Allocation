from .base_allocation import Allocation
import numpy as np
import heapq


class ASMAllocation(Allocation):
    """
    An allocation strategy that prioritizes robots by adaptive submodular maximization
    """

    def allocate(
        self, allocation_metrics, network, successfull_allocations, failed_allocations
    ):
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

        prev_allocations[successfull_allocations] = 1

        alpha = self.cfg.alpha
        beta = self.cfg.beta

        weighted_similarity = (
            alpha * allocation_metrics["state_similarity"]
            + beta * allocation_metrics["action_similarity"]
        )

        uncertainty = allocation_metrics["uncertainty"]

        M = (weighted_similarity * uncertainty).T

        # Based on current allocations find the max M values

        max_M = np.max(M * prev_allocations, axis=1).reshape(-1, 1)

        marginal_contrib = -(np.maximum(max_M, M).sum(axis=0) - max_M.sum())

        marg_contr = [
            (marginal_contrib[i], i)
            for i in range(len(marginal_contrib))
            if i not in failed_allocations and i not in successfull_allocations
        ]

        heapq.heapify(marg_contr)

        # Find the adaptive submodular maximization for the stochastic submodular maximization
        while 1:
            cur_el = heapq.heappop(marg_contr)
            cur_contr = -(
                np.maximum(max_M, M[:, cur_el[1]].reshape(-1, 1)).sum() - max_M.sum()
            ) * network.get_connection_probability(cur_el[1])

            if cur_contr <= marg_contr[0][0]:
                env_priority = cur_el[1]
                max_M = np.maximum(max_M, M[:, cur_el[1]].reshape(-1, 1))
                break
            else:
                heapq.heappush(marg_contr, (cur_contr, cur_el[1]))
        return env_priority
