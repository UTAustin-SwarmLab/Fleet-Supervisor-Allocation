from .base_allocation import Allocation
import numpy as np
import heapq


class ASMAllocation(Allocation):
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

        alpha = self.cfg.alpha

        weighted_similarity = (
            alpha * allocation_metrics["state_similarity"]
            + (1 - alpha) * allocation_metrics["action_similarity"]
        )

        uncertainty = allocation_metrics["uncertainty"]

        M = (weighted_similarity * uncertainty).T

        # Add prioritization for environments that are constraint violating

        constraint_violation = allocation_metrics["constraint_violation"]

        contraint_M = np.eye(M.shape[0]) * constraint_violation

        M = M + self.cfg.constraint_alpha * contraint_M

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
    
