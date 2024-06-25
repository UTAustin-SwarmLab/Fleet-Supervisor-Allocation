from .base_network import BaseNetwork
import numpy as np


class ScarceNetwork(BaseNetwork):
    """
    A network that uses the Drichlet distribution to determine the probability of connection between agents.
    """

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)
        self.connection_probability = (
            np.ones(self.exp_cfg.num_envs) * self.cfg.high_connection_probability
        )
        number_of_low_connection = int(self.exp_cfg.num_envs * self.cfg.mix_ratio)

        # Select random indices to set low connection probability
        low_connection_indices = np.random.choice(
            self.exp_cfg.num_envs, number_of_low_connection, replace=False
        )
        self.connection_probability[low_connection_indices] = self.cfg.low_connection_probability

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"
