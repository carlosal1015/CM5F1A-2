import numpy as np
import matplotlib.pyplot as plt


def casteljau_surface(control_points, u, v):
    n, m, _ = control_points.shape
    q = np.zeros((n, m, 3))
    for i in range(n):
        for j in range(m):
            q[i][j] = control_points[i][j]
    for r in range(n):
        for s in range(m):
            for i in range(n - r - 1):
                for j in range(m - s - 1):
                    q[i][j] = (
                        (1 - u) * (1 - v) * q[i][j]
                        + (1 - u) * v * q[i][j + 1]
                        + u * (1 - v) * q[i + 1][j]
                        + u * v * q[i + 1][j + 1]
                    )
    return q[0][0]


# Puntos de control para la superficie de Bézier (matriz 3x3x3)
control_points = np.array(
    [
        [[0, 0, 0], [1, 0, 2], [2, 0, 1]],
        [[0, 1, 1], [1, 1, 0], [2, 1, 3]],
        [[0, 2, 2], [1, 2, 4], [2, 2, 5]],
    ]
)

# Evaluación de la superficie de Bézier en una cuadrícula de puntos
num_points = 50
u_values = np.linspace(0, 1, num_points)
v_values = np.linspace(0, 1, num_points)
surface_points = np.zeros((num_points, num_points, 3))

for i, u in enumerate(u_values):
    for j, v in enumerate(v_values):
        surface_points[i, j] = casteljau_surface(control_points, u, v)

# Creación de la ilustración con matplotlib
u_grid, v_grid = np.meshgrid(u_values, v_values)
x_points = surface_points[:, :, 0]
y_points = surface_points[:, :, 1]
z_points = surface_points[:, :, 2]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x_points, y_points, z_points, cmap="viridis")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Superficie de Bézier")

plt.show()
