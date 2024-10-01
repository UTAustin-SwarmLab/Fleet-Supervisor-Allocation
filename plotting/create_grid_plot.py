"""
Given the data extracted from the logs, this script creates the paper plots.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns

# Set allocation colors
COLORS = sns.color_palette("tab10")


ALLOCATION_COLORS = {
    "ASA": COLORS[0],
    "NASA": COLORS[1],
    "CUR": COLORS[2],
    "random": COLORS[3],
    "Ensemble": COLORS[4],
    "TD": COLORS[5],
    "NCUR": COLORS[6]
}

MARKERS = {
    "ASA": "o",
    "NASA": "^",
    "CUR": "s",
    "random": "v",
    "Ensemble": "H",
    "TD": "P",
    "NCUR": "D"
}

LINESTYLES = {
    "ASA": "--",
    "NASA": "-",
    "CUR": "--",
    "random": "-.",
    "Ensemble": ":",
    "TD": "--",
    "NCUR": "--",
}

LEGEND_LABELS = {
    "ASA": "ASA",
    "NASA": "n-ASA",
    "CUR": "FD",
    "random": "Random",
    "Ensemble": "FE",
    "TD": "FT",
    "NCUR": "n-FD"
}

metric_names_map = {
    "ROHE": "RoHE",
    "cumulative_successes": "Cumulative Successes",
    "cumulative_human_actions": "Cumulative Human Actions",
    "cumulative_idle_time": "Cumulative\nIdle Time",
    "cumulative_hard_resets": "Cumulative\nHard Resets",
    "cumulative_reward": "Cumulative Reward",
    'cumulative_total_human_actions': "Cumulative Total\nHuman Actions"
}

network_names_map = {
    "base": "Always",
    "scarce": "Mixed-Scarce",
    "real": "Ookla",
    "5G": "5G",
    "changing": "Changing-Scarce"
}

environments_names_map = {
    "AllegroHand": "Allegro Hand",
    "BallBalance": "Ball Balance",
    "Humanoid": "Humanoid",
    "Anymal": "ANYmal"
}


def grid_plot(data, metric, networks, environments, save_dir):

    # Create the save directory if it does not exist
    os.makedirs(save_dir, exist_ok=True)

    # Create a fig, ax object where the number of rows and columns are determined by the number of networks and environments
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(len(networks), len(environments), figsize=(5.5* len(environments), 5 * len(networks)), dpi=600, sharex=True)

    # Extract the data for the given metric 

    metric_data = [d for d in data if d["metric"] == metric]

    # In each subplot, starting with the first subplot, plot the data for each network and environment

    for i, network in enumerate(networks):
        for j, environment in enumerate(environments):
            for allocation_policy in ALLOCATION_COLORS.keys():
                grid_data = []
                for d in metric_data:
                    if d["network"] == network and d["env"] == environment and d["allocation_policy"] == allocation_policy:
                        grid_data.append(d["data"])
                
                if len(grid_data) == 0:
                    if allocation_policy == "TD":
                        if environment == "Anymal" or environment == "Humanoid":
                            continue
                    raise ValueError(f"No data found for {allocation_policy} in {network} and {environment}")
                
                minlen = min([len(d) for d in grid_data])
                grid_data = [d[:minlen] for d in grid_data]
                grid_data_np = np.array(grid_data)
                # Filter out the mean data and the standard deviation data
                mean_data = grid_data_np.mean(axis=0)

                sns.lineplot(
                    x=np.arange(minlen),
                    y=mean_data,
                    color=ALLOCATION_COLORS[allocation_policy],
                    linestyle=LINESTYLES[allocation_policy],
                    marker=MARKERS[allocation_policy],
                    markevery=1000,
                    markersize=12,
                    linewidth=3,
                    ax=ax[i, j]
                )
                std_data = grid_data_np.std(axis=0)
                fill_below = mean_data - std_data/2
                fill_above = mean_data + std_data/2
                fill_below = np.where(fill_below < 0, 0, fill_below)
                fill_above = np.where(fill_above < 0, 0, fill_above)
            
                ax[i, j].fill_between(
                    np.arange(minlen),
                    fill_below,
                    fill_above,
                    alpha=0.3,
                    color=ALLOCATION_COLORS[allocation_policy]
                )
    
    # Remove the y-axis label from all subplots
    for i in range(len(networks)):
        for j in range(len(environments)):
            ax[i, j].set_ylabel("")

    # Add the y axis label only to the first column of subplots
    for i in range(len(networks)):
        ax[i, 0].set_ylabel(metric_names_map[metric], fontsize=24, fontweight='bold')
    
    # Make the tick labels bigger and bolder
    for i in range(len(networks)):
        for j in range(len(environments)):
            ax[i, j].tick_params(axis='both', which='major', labelsize=16, width=3)
            for tick in ax[i, j].get_xticklabels():
                tick.set_fontsize(18)
            for tick in ax[i, j].get_yticklabels():
                tick.set_fontsize(18)
    
    # Add the x-axis label only to the last row of subplots
    for j in range(len(environments)):
        ax[len(networks) - 1, j].set_xlabel("Time Steps (t)", fontsize=21, fontweight='bold')

    # Save the plot
    plt.tight_layout()
    save_loc = os.path.join(save_dir, f"{metric}.png")

    plt.savefig(save_loc, bbox_inches="tight")


def grid_plot_rohe(data, metric, networks, environments, save_dir):

    # Create the save directory if it does not exist
    os.makedirs(save_dir, exist_ok=True)

    # Create a fig, ax object where the number of rows and columns are determined by the number of networks and environments
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(len(networks), len(environments), figsize=(6* len(environments), 5 * len(networks)), dpi=600, sharex=True)

    # Extract the data for the given metric 

    metric_data = [d for d in data if d["metric"] == metric]

    # In each subplot, starting with the first subplot, plot the data for each network and environment

    for i, network in enumerate(networks):
        for j, environment in enumerate(environments):
            for allocation_policy in ALLOCATION_COLORS.keys():
                grid_data = []
                for d in metric_data:
                    if d["network"] == network and d["env"] == environment and d["allocation_policy"] == allocation_policy:
                        grid_data.append(d["data"])
                
                if len(grid_data) == 0:
                    if allocation_policy == "TD":
                        if environment == "Anymal" or environment == "Humanoid":
                            continue
                    raise ValueError(f"No data found for {allocation_policy} in {network} and {environment}")
                
                minlen = min([len(d) for d in grid_data])
                grid_data = [d[:minlen] for d in grid_data]
                grid_data_np = np.array(grid_data)
                # Filter out the mean data and the standard deviation data
                mean_data = grid_data_np.mean(axis=0)

                sns.lineplot(
                    x=np.arange(minlen),
                    y=mean_data,
                    color=ALLOCATION_COLORS[allocation_policy],
                    linestyle=LINESTYLES[allocation_policy],
                    marker=MARKERS[allocation_policy],
                    markevery=1000,
                    markersize=12,
                    linewidth=3,
                    ax=ax[i, j]
                )
                std_data = grid_data_np.std(axis=0)
                fill_below = mean_data - std_data/2
                fill_above = mean_data + std_data/2
                fill_below = np.where(fill_below < 0, 0, fill_below)
                fill_above = np.where(fill_above < 0, 0, fill_above)
            
                ax[i, j].fill_between(
                    np.arange(minlen),
                    fill_below,
                    fill_above,
                    alpha=0.3,
                    color=ALLOCATION_COLORS[allocation_policy]
                )
    
    # Remove the y-axis label from all subplots
    for i in range(len(networks)):
        for j in range(len(environments)):
            ax[i, j].set_ylabel("")

    # Add the y axis label only to the first column of subplots
    for i in range(len(networks)):
        ax[i, 0].set_ylabel(metric_names_map[metric], fontsize=24, fontweight='bold')
    
    # Make the tick labels bigger and bolder
    for i in range(len(networks)):
        for j in range(len(environments)):
            ax[i, j].tick_params(axis='both', which='major', labelsize=16, width=3)
            for tick in ax[i, j].get_xticklabels():
                tick.set_fontsize(18)
            for tick in ax[i, j].get_yticklabels():
                tick.set_fontsize(18)
    
    # Add the x-axis label only to the last row of subplots
    for j in range(len(environments)):
        ax[len(networks) - 1, j].set_xlabel("Time Steps (t)", fontsize=21, fontweight='bold')

    # Save the plot
    plt.tight_layout()
    save_loc = os.path.join(save_dir, f"{metric}.png")

    plt.savefig(save_loc, bbox_inches="tight")
