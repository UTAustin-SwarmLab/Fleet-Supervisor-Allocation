import numpy as np

class BaseNetwork:
    """
    Base class for all network types.
    """

    connection_probability : np.ndarray

    def __init__(self, exp_cfg):
        self.exp_cfg = exp_cfg
        self.cfg = exp_cfg.network_cfg

    def get_connection_probability(self, agent_idx):
        """Get connection probability for an agent."""
        return self.connection_probability[agent_idx]
