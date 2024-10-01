"""
Plot given a parent logdir where each subdirectory is an experiment logdir 
(and each is replicated 3x for 3 seeds)
and a statistic (e.g., cumulative_successes, ROHE)
"""

import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
import os
import seaborn as sns
import json

# Set allocation colors
colors = sns.color_palette("tab10")

allocation_colors = {
    "ASA": colors[0],
    "NASA": colors[1],
    "CUR": colors[2],
    "Random": colors[3],
    "Ensemble": colors[4],
    "TD": colors[5],
    "NCUR": colors[6]
}

markers = {
    "ASA": "o",
    "NASA": "^",
    "CUR": "s",
    "Random": "v",
    "Ensemble": "H",
    "TD": "P",
    "NCUR": "D"
}

line_styles = {
    "ASA": "--",
    "NASA": "-",
    "CUR": "--",
    "Random": "-.",
    "Ensemble": ":",
    "TD": "--",
    "NCUR": "--",
}

legend_labels = {
    "ASA": "ASA",
    "NASA": "n-ASA",
    "CUR": "FD",
    "Random": "Random",
    "Ensemble": "FE",
    "TD": "FT",
    "NCUR": "FD"
}

def plot(colors, markers, line_styles, legend_labels):
    if len(sys.argv) != 3:
        assert False, "usage: python plot.py [logdir] [key]"


    directory = sys.argv[1]
    KEY = sys.argv[2]  # e.g. 'cumulative_successes'

    files = sorted(os.listdir(directory), key=lambda x: x[::-1])
    filesdatas = [
        pickle.load(
            open(directory + "/" + f + "/run_stats.pkl", "rb")
        )[KEY] for f in files
    ]

    minlen = min([len(fd) for fd in filesdatas])
    filedatas = [fd[:minlen] for fd in filesdatas]

    allocation_keys = []
    for file in files:
        if "ASA" in file and "NASA" not in file:
            allocation_keys.append("ASA")
        elif "TD" in file:
            allocation_keys.append("TD")
        elif "NASA" in file:
            allocation_keys.append("NASA")
        elif "CUR" in file and "NCUR" not in file:
            allocation_keys.append("CUR")
        elif "random" in file:
            allocation_keys.append("Random")
        elif "Ensemble" in file:
            allocation_keys.append("Ensemble")
        elif "NCUR" in file:
            allocation_keys.append("NCUR")

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=600)

    final_values = {}
    for i in range(0, len(files), 3):
        data = np.array(filedatas[i : i + 3])
        if KEY == "ROHE":
            data = data * 100
        mean_data = data.mean(axis=0)
        
        final_value = mean_data[-1]
        final_values[allocation_keys[i]] = final_value

        sns.lineplot(
            x=np.arange(minlen),
            y=mean_data,
            #label=legend_labels[allocation_keys[i]],
            color=allocation_colors[allocation_keys[i]],
            linestyle=line_styles[allocation_keys[i]],
            marker=markers[allocation_keys[i]],
            markevery=1000,
            markersize=12,
            linewidth=3,
            ax=ax
        )

        fill_below = mean_data - data.std(axis=0)/2
        fill_above = mean_data + data.std(axis=0)/2

        # to avoid negative values due to std_deviation
        fill_below = np.where(fill_below < 0, 0, fill_below) 
        fill_above = np.where(fill_above < 0, 0, fill_above)

        ax.fill_between(
            np.arange(minlen),
            fill_below,
            fill_above,
            alpha=0.3,
            color=allocation_colors[allocation_keys[i]],
        )

    # Remove the y-axis label
    #ax.set_ylabel("RoHE", fontsize=20, fontweight='bold')
    ax.set_ylabel("")

    # Add and style the x-axis label
    #ax.set_xlabel("Time Steps (t)", fontsize=20, fontweight='bold')
    ax.set_ylabel("RoHE", fontsize=20, fontweight='bold')

    # Make the tick labels bigger and bolder
    ax.tick_params(axis='both', which='major', labelsize=14, width=2)
    for tick in ax.get_xticklabels():
        tick.set_fontweight('bold')
        tick.set_fontsize(18)

    for tick in ax.get_yticklabels():
        tick.set_fontweight('bold')
        tick.set_fontsize(18)
    
    # plt.title('{}'.format(KEY))
    parent_dir = os.path.dirname(os.getcwd())
    
    plt.savefig(
        os.path.join(parent_dir, "{}.jpg".format(KEY)), 
            bbox_inches="tight"
        )

if __name__ == "__main__":
    plot(colors, markers, line_styles, legend_labels)

    print("Plot saved;")
    print(f"{os.path.join(os.path.dirname(os.getcwd()), sys.argv[2] + '.jpg')}")