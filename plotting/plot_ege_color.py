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

ASM_color = 'red'
NASM_color = "blue"
CUR_color = 'green'
RD_color = 'orange'
TD_color = 'cyan'
EN_color = 'purple'

assigned_colors = {"ASM": ASM_color, "U.C.G": TD_color, "NASM": NASM_color, "CUR": CUR_color, "Random": RD_color, "U.C": EN_color}

if len(sys.argv) < 3:
    assert False, "usage: python plot.py [logdir] [key]"
directory = sys.argv[1]
KEY = sys.argv[2]  # e.g. 'cumulative_successes'
files = sorted(os.listdir(directory), key=lambda x: x[::-1])
filedatas = [
    pickle.load(open(directory + "/" + f + "/run_stats.pkl", "rb"))[KEY] for f in files
]
minlen = min([len(fd) for fd in filedatas])
filedatas = [fd[:minlen] for fd in filedatas]
if len(sys.argv) == 4:
    KEY2 = sys.argv[3]
    filedatas2 = [
        pickle.load(open(directory + "/" + f + "/run_stats.pkl", "rb"))[KEY2]
        for f in files
    ]
    filedatas2 = [fd[:minlen] for fd in filedatas2]

color_codes = []
labels = []
allocation_keys = []
for file in files: 
    if "ASM" in file and "NASM" not in file:
        labels.append("ASM")
    elif "TD" in file:
        labels.append("U.C.G")
    elif "NASM" in file:
        labels.append("NASM")
    elif "CUR" in file:
        labels.append("CUR") 
    elif "random" in file:
        labels.append("Random")
    elif "Ensemble" in file:
        labels.append("U.C")

set_plot_properties()

fig, ax = plt.subplots(figsize=(10, 5), dpi=600)

for i in range(0, len(files), 5):
    label = "{}".format(files[i][files[i].rindex("_") + 1 :])
    data = np.array(filedatas[i : i + 5])
    if len(sys.argv) == 4:
        data2 = np.array(filedatas2[i : i + 5])
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
