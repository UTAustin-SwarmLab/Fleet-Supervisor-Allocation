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
    "NCUR": colors[3],
    "NCUR_0.6": colors[4],
    "NCUR_0.3":colors[5],
    "NCUR_0.4":colors[6],
}

markers = {
    "ASM": "o",
    "NASM": "^",
    "CUR": "s",
    "NCUR": "o",
    "NCUR_0.6": "^",
    "NCUR_0.4":"v",
    "NCUR_0.3":"h",
}

line_styles = {
    "ASM": "--",
    "NASM": "-",
    "CUR": "--",
    "NCUR": ":",
    "NCUR_0.6": "-",
    "NCUR_0.4":"-.",
    "NCUR_0.3":"-.",
}

legend_labels = {
    "ASM": "ASA",
    "NASM": "n-ASA",
    "NCUR": "FD(connection threshold > 0.2)",
    "NCUR_0.6": "FD(connection threshold=0.6)",
    "NCUR_0.4": "FD(connection threshold=0.4)",
    "NCUR_0.3": "FD(connection threshold=0.3)",
    "CUR": "FD"
}

def plot(colors, markers, line_styles, legend_labels):
    if len(sys.argv) < 3:
        assert False, "usage: python plot.py [logdir] [key]"


    directory = sys.argv[1]
    KEY = sys.argv[2]  # e.g. 'cumulative_successes'
    special_network = False
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
        if special_network:
            if "NCUR" in file:
                allocation_keys.append("NCUR")
            elif "CUR" in file and "NCUR" not in file:
                allocation_keys.append("CUR")
            elif "ASM" and "NASM" not in file:
                allocation_keys.append("ASM")
            elif "NASM" in file:
                allocation_keys.append("NASM")
        else:
            if (
                "NCUR" in file 
                and "0.6" not in file 
                and "0.3" not in file 
                and "0.4" not in file
            ):
                allocation_keys.append("NCUR")
            elif "CUR" in file and "NCUR" not in file:
                allocation_keys.append("CUR")
            elif "NCUR_0.6" in file:
                allocation_keys.append("NCUR_0.6")
            elif "NCUR_0.4" in file:
                allocation_keys.append("NCUR_0.4")
            elif "NCUR_0.3" in file:
                allocation_keys.append("NCUR_0.3")
            elif "ASM" and "NASM" not in file:
                allocation_keys.append("ASM")
            elif "NASM" in file:
                allocation_keys.append("NASM")
        
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=600)

    for i in range(0, len(files), 3):
        data = np.array(filedatas[i : i + 3])
        if KEY == "ROHE":
            data = data * 100
        mean_data = data.mean(axis=0)
        
        sns.lineplot(
            x=np.arange(minlen),
            y=mean_data,
            #label=legend_labels[allocation_keys[i]],
            color=allocation_colors[allocation_keys[i]],
            linestyle=line_styles[allocation_keys[i]],
            marker=markers[allocation_keys[i]],
            markevery=1000,
            markersize=10,
            linewidth=3,
            ax=ax
        )

        
        fill_below = (mean_data - data.std(axis=0)/2)
        fill_above = (mean_data + data.std(axis=0)/2)

        # to avoid negative values due to std_deviation
        fill_below = np.where(fill_below < 0, 0, fill_below) 
        fill_above = np.where(fill_above < 0, 0, fill_above)

        ax.fill_between(
            np.arange(minlen),
            fill_below,
            fill_above,
            alpha=0.2,
            color=allocation_colors[allocation_keys[i]],
        )

    ax.set_xlabel("Time Steps (t)")
    ax.set_ylabel(KEY.replace("_", " ").title())
    #ax.legend()


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
