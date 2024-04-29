"""
Plot given a parent logdir where each subdirectory is an experiment logdir (and each is replicated 3x for 3 seeds)
and a statistic (e.g., cumulative_successes, cumulative_viols, cumulative_idle_time)
"""

import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
import os
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties
from swarm_visualizer.utility.general_utils import set_axis_infos

allocation_colors = {  
    "ASM":"red", 
    "NASM":"blue", 
    "CUR":"green", 
    "RANDOM":"orange", 
    "BC":"cyan", 
    "ED":"purple", 
    "U.C.G": "yellow"
    }

assigned_colors = {
    "ASM": allocation_colors["ASM"],
    "NASM": allocation_colors["NASM"],
    "CUR": allocation_colors["CUR"],
    "RANDOM": allocation_colors["RANDOM"],
    "U.C": allocation_colors["ED"],
    "B.C": allocation_colors["BC"] ,
    "U.C.G": allocation_colors["U.C.G"]
}

if len(sys.argv) < 3:
    assert False, "usage: python plot.py [logdir] [key]"
directory = sys.argv[1]
KEY = sys.argv[2]  # e.g. 'cumulative_successes'
files = sorted(os.listdir(directory), key=lambda x: x[::-1])

if KEY == "ROHE":
    key1 = "cumulative_successes"
    key2 = "cumulative_human_actions"
    filesdatas1 = [
        pickle.load(open(directory + "/" + f + "/run_stats.pkl", "rb"))[key1]
        for f in files
    ]
    filesdatas2 = [
        pickle.load(open(directory + "/" + f + "/run_stats.pkl", "rb"))[key2]
        for f in files
    ]

    minlen = min([len(fd) for fd in filesdatas1])
    filedatas1 = [fd[:minlen] for fd in filesdatas1]
    filedatas2 = [fd[:minlen] for fd in filesdatas2]

    filedatas = []
    for i in range(len(filesdatas1)):
        fd = []
        for j in range(len(filedatas1[i])):
            fd.append(filedatas1[i][j] / (filedatas2[i][j] + 1))
        filedatas.append(fd)
else:
    filesdatas = [
        pickle.load(open(directory + "/" + f + "/run_stats.pkl", "rb"))[KEY]
        for f in files
    ]
    minlen = min([len(fd) for fd in filesdatas])
    filedatas = [fd[:minlen] for fd in filesdatas]

if len(sys.argv) == 4:
    KEY2 = sys.argv[3]
    filedatas2 = [
        pickle.load(open(directory + "/" + f + "/run_stats.pkl", "rb"))[KEY2]
        for f in files
    ]
    filedatas2 = [fd[:minlen] for fd in filedatas2]

labels = []
allocation_keys = []
legend_labels = []
for file in files:
    if "ASM" in file and "NASM" not in file:
        labels.append("ASM")
        legend_labels.append("ASM")
    elif "TD" in file:
        labels.append("U.C.G")
        legend_labels.append("U.C.G")
    elif "BC" in file:
        labels.append("B.C")
        legend_labels.append("B.C")
    elif "NASM" in file:
        labels.append("NASM")
        legend_labels.append("NASM")
    elif "CUR" in file:
        labels.append("CUR")
        legend_labels.append("CUR")
    elif "random" in file:
        labels.append("RANDOM")
        legend_labels.append("random")
    elif "Ensemble" in file:
        labels.append("U.C")
        legend_labels.append("U.C")

set_plot_properties()

fig, ax = plt.subplots(figsize=(10, 5), dpi=600)

for i in range(0, len(files), 1):
    label = legend_labels[i]
    data = np.array(filedatas[i : i + 1])
    if len(sys.argv) == 4:
        data2 = np.array(filedatas2[i : i + 1])
        LAMBDA = 0.01
        data = data - LAMBDA * data2
    plt.plot(data.mean(axis=0), label=label, color=assigned_colors[labels[i]])
    plt.fill_between(
        np.arange(minlen),
        data.mean(axis=0) - data.std(axis=0),
        data.mean(axis=0) + data.std(axis=0),
        alpha=0.2,
        color=assigned_colors[labels[i]],
    )
plt.legend()

set_axis_infos(ax, "Time Steps (t)", KEY.replace("_", " ").title())

if len(sys.argv) == 4:
    # plt.title('{}-{}'.format(KEY, KEY2))
    plt.savefig("cumulative_diff.jpg".format(KEY, KEY2), bbox_inches="tight")
else:
    # plt.title('{}'.format(KEY))
    plt.savefig("{}.jpg".format(KEY), bbox_inches="tight")
