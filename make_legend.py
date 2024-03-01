from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties
from swarm_visualizer.utility.general_utils import set_axis_infos
from swarm_visualizer.utility.legendplot_utils import create_seperate_legend

BC_color = "#984ea3"


labels = ["Random", "FE", "FT", "FD", "ASM"]
colors = ["#a65628", "#4daf4a", "#ff7f00", "#f781bf", "#377eb8"]
linetypes = ["-", "-", "-", "-", "-"]
legend_size = [4.5, 0.3]
legend_n_col = 5
linewidth = 4

# Create a separate legend
create_seperate_legend(
    labels,
    colors,
    linetypes,
    linewidth=linewidth,
    legend_size=legend_size,
    legend_n_col=legend_n_col,
    save_loc="./legend.png",
)
