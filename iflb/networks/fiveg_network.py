from .base_network import BaseNetwork
import numpy as np
import pandas as pd
import os


class FiveGNetwork(BaseNetwork):
    """
    A network that uses the real network to determine the probability of connection between agents using the real network
    data.
    """

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)

        # Load 5G network data
        script_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(script_directory, "data")
        fiveg_network_data_path = os.path.join(data_directory, "ATNT_data.csv")

        self.fiveg_network_data = pd.read_csv(fiveg_network_data_path)

        # Group the data into num_envs groups and calculate the mean of each group
        self.fiveg_network_data_grouped = self.fiveg_network_data.groupby(
            np.arange(len(self.fiveg_network_data)) // self.exp_cfg.num_envs
        ).mean()

        self.fiveg_network_data_grouped["iteration"] = self.fiveg_network_data_grouped.index

        # Get the latency and throughput data

        latency_data = self.fiveg_network_data_grouped[self.cfg.latency_key].values
        throughput_data = self.fiveg_network_data_grouped[self.cfg.throughput_key].values

        # Normalize the latency data to be between 0 and 1
        latency_data = (latency_data - latency_data.min()) / (
            latency_data.max() - latency_data.min()
        )

        # Log normalize the throughput data
        throughput_data = np.log(throughput_data + 1)
        throughput_data = (throughput_data - throughput_data.min()) / (
            throughput_data.max() - throughput_data.min()
        )

        # Create the connection probability matrix
        self.connection_probability = throughput_data

        # Get the locations where the latency is greater than the threshold and 
        # the throughput is less than the threshold
        latency_viols = latency_data > self.cfg.latency_upper_limit
        throughput_viols = throughput_data < self.cfg.throughput_lower_limit

        # Set the connection probability with the scaled wrt to the lower bound

        self.connection_probability = throughput_data * (1 - self.cfg.lower_bound) + self.cfg.lower_bound

        # Set the connection probability to 0 if the latency or throughput is greater than the threshold
        self.connection_probability[latency_viols | throughput_viols] = self.cfg.low_probability

        np.random.shuffle(self.connection_probability)

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"

        assert np.all(
            self.connection_probability >= 0
        ), "Connection probability should be greater than 0"

        assert len(self.connection_probability) == self.exp_cfg.num_envs, \
        "Connection probability should have the same length as the number of environments"
