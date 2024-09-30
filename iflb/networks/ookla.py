"""Ookla Network."""

import os

import numpy as np
import pandas as pd

from .always import BaseNetwork


class OoklaNetwork(BaseNetwork):
    """
    A network that uses the real network to determine the probability of connection between agents using the real network
    data.
    """

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)

        # Load the real network data
        script_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(script_directory, "data")
        real_network_data_path = os.path.join(data_directory, "region_stats_a.csv")

        self.real_network_data = pd.read_csv(real_network_data_path)

        network_data = self.real_network_data[self.cfg.real_network_data_key].values

        network_data = network_data[: self.exp_cfg.num_envs]

        # If the network data is less than self.exp_cfg.num_envs, then raise an error
        assert len(network_data) == self.exp_cfg.num_envs, "Network data is less than the number of environments"

        network_data = np.log(network_data + 1)

        # Normalize the network data to be between 0 and 1
        network_data = (network_data - network_data.min()) / (
            (1 / (1 - self.cfg.lower_bound)) * (network_data.max() - network_data.min())
        ) + self.cfg.lower_bound

        self.connection_probability = network_data

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"
