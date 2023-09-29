import numpy as np
import matplotlib.pyplot as plt


def casteljau_surface(control_points, u, v):
    n, m, _ = control_points.shape
    q = np.zeros((n, m, 3))
    intermediate_results = [control_points.copy()]
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
            intermediate_results.append(q.copy())
    return q, intermediate_results


# Puntos de control para la superficie de Bézier (matriz 3x3x3)
control_points = np.array(
    [
        [[0, 0, 0], [1, 0, 2], [2, 0, 1]],
        [[0, 1, 1], [1, 1, 0], [2, 1, 3]],
        [[0, 2, 2], [1, 2, 4], [2, 2, 5]],
    ]
)

# Evaluación de la superficie de Bézier en un punto específico (u=0.5, v=0.5)
u = 0.5
v = 0.5
final_result, intermediate_results = casteljau_surface(control_points, u, v)

# Creación de la visualización de las etapas intermedias
fig, axes = plt.subplots(1, len(intermediate_results), figsize=(15, 5))
for i, intermediate_result in enumerate(intermediate_results):
    ax = axes[i]
    ax.imshow(
        intermediate_result[:, :, 0],
        cmap="viridis",
        origin="lower",
        extent=[0, 2, 0, 2],
    )
    ax.set_title(f"Step {i}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
plt.show()

# Mostrar el resultado final
print(f"Punto evaluado en (u={u}, v={v}): {final_result}")
