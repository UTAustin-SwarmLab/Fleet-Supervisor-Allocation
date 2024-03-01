# This python file generates a toy example of a 2D state space model and allocation
# policy for the selecting the best location for human supervisor. Here we compare
# the performance of the proposed method with the uncertarinty based method.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties
from swarm_visualizer.utility.general_utils import set_axis_infos

# Generate x and y coordinates for the state space

x = np.linspace(0, 10, 1000)
y = np.linspace(0, 10, 1000)

# Create 3 gaussian blobs in the 2d space with different means and covariance matrices
# Calculate the heat map based on the gaussian blobs and covariance


def gaussian(x, y, x0, y0, xalpha, yalpha, magnitude):
    return magnitude * np.exp(
        -(((x - x0) / xalpha) ** 2 + ((y - y0) / yalpha) ** 2) / 2
    )


x_means = [3, 7, 6, 3, 9, 5, 6]
y_means = [6, 7, 3, 2, 4, 9, 5]
x_alpha = [1, 1, 1, 1.5, 1, 1.5, 1]
y_alpha = [1, 1, 1, 1.5, 1, 1.5, 1]
magnitudes = [2, 1.5, 1, 2, 2, 1.5, 1.5]

X, Y = np.meshgrid(x, y)
Z = np.zeros(X.shape)

for i in range(len(x_means)):
    Z += gaussian(X, Y, x_means[i], y_means[i], x_alpha[i], y_alpha[i], magnitudes[i])


set_plot_properties()

# Plot the heat map of the state space
fig, ax = plt.subplots(figsize=(10, 5), dpi=600)
# sns.heatmap(Z, cmap="Greens", ax=ax)
plt.contourf(X, Y, Z, cmap="Blues")
cbar = plt.colorbar()
cbar.set_label("Uncertainty", fontsize=30)

# Select 10 samples from the states spaces with 3 points from highest gaussian blob

unc_mean_x = [3, 9, 3]
unc_mean_y = [6, 4, 2]
unc_var_x = [0.1, 0.1, 0.1]
unc_var_y = [0.1, 0.1, 0.1]
n_points_unc = 7

unc_x_points = np.zeros(n_points_unc * len(unc_mean_x))
unc_y_points = np.zeros(n_points_unc * len(unc_mean_x))
for i in range(len(unc_mean_x)):
    unc_x_points[i * n_points_unc : (i + 1) * n_points_unc] = np.random.normal(
        unc_mean_x[i], unc_var_x[i], n_points_unc
    )
    unc_y_points[i * n_points_unc : (i + 1) * n_points_unc] = np.random.normal(
        unc_mean_y[i], unc_var_y[i], n_points_unc
    )

sm_mean_x = [3, 3, 5, 6, 7, 9, 6]
sm_mean_y = [6, 2, 9, 3, 7, 4, 5]
sm_var_x = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
sm_var_y = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
n_points_sm = 3

sm_x_points = np.zeros(n_points_sm * len(sm_mean_x))
sm_y_points = np.zeros(n_points_sm * len(sm_mean_x))
for i in range(len(sm_mean_x)):
    sm_x_points[i * n_points_sm : (i + 1) * n_points_sm] = np.random.normal(
        sm_mean_x[i], sm_var_x[i], n_points_sm
    )
    sm_y_points[i * n_points_sm : (i + 1) * n_points_sm] = np.random.normal(
        sm_mean_y[i], sm_var_y[i], n_points_sm
    )


print("Points selected by the submodular maximization method")

# Plot the points selected by the submodular maximization and uncertainty based methods increase the
# size of the points and make them distinct by color and make them thicker
plt.scatter(
    unc_x_points,
    unc_y_points,
    c="magenta",
    marker="x",
    s=300,
    linewidths=4,
    label="Score Based",
)
plt.scatter(
    sm_x_points,
    sm_y_points,
    c="yellow",
    marker="+",
    s=300,
    linewidths=4,
    label="Submodular Maximization",
)
plt.legend()

# plt.xlabel("X")
# plt.ylabel("Y")

# Set axis infos
set_axis_infos(ax, xlabel_size=30, ylabel_size=30, title_size=30)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.tight_layout()

plt.savefig("toy_example.png")
