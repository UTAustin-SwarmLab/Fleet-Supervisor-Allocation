"""Dirichlet Network module."""

import numpy as np

from .always import BaseNetwork


class DirichletNetwork(BaseNetwork):
    """
    A network that uses the Drichlet distribution.
    """

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)
        self.connection_probability = np.random.dirichlet(
            np.repeat(self.cfg.dirichlet_alpha, 2), (self.exp_cfg.num_envs)
        )[:, 0]

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"
