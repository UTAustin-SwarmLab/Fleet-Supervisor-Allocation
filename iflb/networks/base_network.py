import numpy as np


class BaseNetwork:
    """
    Base class for all network types.
    """

    def __init__(self, exp_cfg):
        self.exp_cfg = exp_cfg
        self.cfg = exp_cfg.network_cfg

        self.connection_probability = np.ones(self.exp_cfg.num_envs)

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"

    def get_connection_probability(self, agent_idx):

        return self.connection_probability[agent_idx]
