import matplotlib.pyplot as plt
import seaborn as sns

# Set allocation colors
colors = sns.color_palette("tab10")

allocation_colors = {
    "ASM": colors[0],
    "NASM": colors[1],
    "CUR": colors[2],
    "NCUR": colors[3],
    "NCUR_0.6": colors[4],
    "NCUR_0.3": colors[5],
    "NCUR_0.4": colors[6],
    "NCUR_0.2": colors[7],
}

markers = {
    "ASM": "o",
    "NASM": "^",
    "CUR": "s",
    "NCUR": "o",
    "NCUR_0.6": "^",
    "NCUR_0.4": "v",
    "NCUR_0.3": "h",
    "NCUR_0.2": "o",
}

line_styles = {
    "ASM": "--",
    "NASM": "-",
    "CUR": "--",
    "NCUR": ":",
    "NCUR_0.6": "-",
    "NCUR_0.4": "-.",
    "NCUR_0.3": "-.",
    "NCUR_0.2": ":"
}

legend_labels = {
    "ASM": "ASA",
    "NASM": "n-ASA",
    "NCUR": "FD(connection threshold=0.7)",
    "NCUR_0.6": "FD(connection threshold=0.6)",
    "NCUR_0.4": "FD(connection threshold=0.4)",
    "NCUR_0.3": "FD(connection threshold=0.3)",
    "CUR": "FD",
    "NCUR_0.2": "FD(connection threshold\u22650.2)",
}

# Create a dummy plot to generate the legend
fig, ax = plt.subplots()

for key in allocation_colors.keys():
    ax.plot([], [], 
            label=legend_labels[key], 
            color=allocation_colors[key], 
            linestyle=line_styles[key], 
            marker=markers[key], 
            markersize=10, 
            linewidth=2)

# Create the legend
legend = ax.legend(loc='center', frameon=False)

# Create a new figure for the legend
fig_legend = plt.figure(figsize=(8, 4))
ax_legend = fig_legend.add_subplot(111)
ax_legend.axis('off')
legend = ax_legend.legend(*ax.get_legend_handles_labels(), loc='center', frameon=False)

# Save the legend as a PNG file
fig_legend.savefig("legend.png", bbox_inches='tight', dpi=600)

plt.close(fig)
plt.close(fig_legend)