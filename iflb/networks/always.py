import numpy as np
from .base import BaseNetwork

class AlwaysNetwork(BaseNetwork):
    """A network that always connects agents."""

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)
        self.connection_probability = np.ones(self.exp_cfg.num_envs)

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"
