from .base_network import BaseNetwork
import numpy as np


class DirichletNetwork(BaseNetwork):
    """
    A network that uses the Drichlet distribution to determine the probability of connection between agents.
    """

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)
        self.connection_probability = np.random.dirichlet(
            np.repeat(self.cfg.dirichlet_alpha, 2), (self.exp_cfg.num_envs)
        )[:, 0]

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"
