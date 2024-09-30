import numpy as np
from .base import BaseNetwork


class ChangingScarceNetwork(BaseNetwork):
    """Network with changing connection probabilities."""

    def __init__(self, exp_cfg):
        super().__init__(exp_cfg)
        self.connection_probability = (
            np.ones(self.exp_cfg.num_envs) * self.cfg.high_connection_probability
        )
        print("initialized")
        number_of_low_connection = int(self.exp_cfg.num_envs * self.cfg.mix_ratio)

        # Select random indices to set low connection probability
        self.low_connection_indices = np.random.choice(
            self.exp_cfg.num_envs, number_of_low_connection, replace=False
        )
        self.high_connection_indices = np.array(
            [i for i in range(self.exp_cfg.num_envs) if i not in self.low_connection_indices]
        )
        self.connection_probability[self.low_connection_indices] = self.cfg.low_connection_probability

        assert np.all(
            self.connection_probability <= 1
        ), "Connection probability should be less than 1"
    
    def change_connection_probability(self, time_step):
        """Change connection probabilities according to time step."""

        # If time step is less than change start time do nothing

        if time_step < self.cfg.change_start_time * self.exp_cfg.num_steps:
            return
        
        # If time step is greater than change end time switch to high connection probability change 
        # connection probability to high connection probability

        if time_step > self.cfg.change_end_time * self.exp_cfg.num_steps:
            self.connection_probability[self.low_connection_indices] = self.cfg.high_connection_probability
            self.connection_probability[self.high_connection_indices] = self.cfg.low_connection_probability
            return
        
        # If time step is between change start time and change end time change connection probability 
        # linearly from low to high connection probability

        time_step_ratio = (time_step - self.cfg.change_start_time * self.exp_cfg.num_steps) / \
        ((self.cfg.change_end_time - self.cfg.change_start_time) * self.exp_cfg.num_steps)

        self.connection_probability[self.low_connection_indices] = self.cfg.low_connection_probability + \
        (self.cfg.high_connection_probability - self.cfg.low_connection_probability) * time_step_ratio

        self.connection_probability[self.high_connection_indices] = self.cfg.high_connection_probability - \
        (self.cfg.high_connection_probability - self.cfg.low_connection_probability) * time_step_ratio
