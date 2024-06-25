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

# Set allocation colors
colors = sns.color_palette("tab10")

allocation_colors = {
    "ASM": colors[0],
    "NASM": colors[1],
    "CUR": colors[2],
    "Random": colors[3],
    "Ensemble": colors[4],
    "TD": colors[5],
}

markers = {
    "ASM": "o",
    "NASM": "^",
    "CUR": "s",
    "Random": "v",
    "Ensemble": "H",
    "TD": "P",
}

line_styles = {
    "ASM": "--",
    "NASM": "-",
    "CUR": "--",
    "Random": "-.",
    "Ensemble": ":",
    "TD": "--",
}

legend_labels = {
    "ASM": "ASA",
    "NASM": "n-ASA",
    "CUR": "FD",
    "Random": "Random",
    "Ensemble": "FE",
    "TD": "FT",
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
        if "ASM" in file and "NASM" not in file:
            allocation_keys.append("ASM")
        elif "TD" in file:
            allocation_keys.append("TD")
        elif "NASM" in file:
            allocation_keys.append("NASM")
        elif "CUR" in file:
            allocation_keys.append("CUR")
        elif "Random" in file:
            allocation_keys.append("Random")
        elif "Ensemble" in file:
            allocation_keys.append("Ensemble")

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=600)

    for i in range(0, len(files), 1):
        data = np.array(filedatas[i : i + 1])
        if KEY == "ROHE":
            data = data * 100
        mean_data = data.mean(axis=0)
        
        sns.lineplot(
            x=np.arange(minlen),
            y=mean_data,
            label=legend_labels[allocation_keys[i]],
            color=allocation_colors[allocation_keys[i]],
            linestyle=line_styles[allocation_keys[i]],
            marker=markers[allocation_keys[i]],
            markevery=1000,
            markersize=10,
            linewidth=3,
            ax=ax
        )

        fill_below = mean_data - data.std(axis=0) 
        fill_above = mean_data + data.std(axis=0)

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

    ax.set_xlabel("Time Steps (t)")
    ax.set_ylabel(KEY.replace("_", " ").title())
    ax.legend()


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