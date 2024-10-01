# This function creates paper plots

from plotting.extract_data_from_logs import extract_data_from_logs
from plotting.create_grid_plot import grid_plot_rohe, grid_plot


logs_dir = "/nas/oguzhan/fleet_supervision/logs"

metrics_to_extract = ["ROHE", "cumulative_successes", 
                      "cumulative_total_human_actions", "cumulative_idle_time",
                        "cumulative_hard_resets", "cumulative_reward" ]

allocation_policies = [
    "NCUR",
    "CUR",
    "NASA",
    "ASA",
    "random",
    "Ensemble",
    "TD"
]

environments = [
    "AllegroHand",
    "BallBalance",
    "Humanoid",
    "Anymal"
]

networks = [
    "base",
    "scarce",
    "real",
    "5G",
    "changing",
]

data = extract_data_from_logs(logs_dir, metrics_to_extract, allocation_policies, environments, networks)

# Create the paper plots

for metric in metrics_to_extract:
    grid_plot(data, metric, networks, environments, "./paper_plots")


grid_plot_rohe(data, "ROHE", networks, environments, "./paper_plots")
