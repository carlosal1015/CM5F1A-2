#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

x = np.arange() - np.pi
# I = np.concatenate((I_0, I_1, I_2), axis=None)


# def plot():
#     x = np.array([0, 1, 2, 3])
#     y = np.array([1, 1, 0, 10])
#     plt.cla()
#     plt.plot(I_0, S_0, lw=0.45, label=f"$S_0(x)$")
#     plt.plot(I_1, S_1, lw=0.45, label=f"$S_1(x)$")
#     plt.plot(I_2, S_2, lw=0.45, label=f"$S_2(x)$")
#     plt.scatter(x, y, s=10, label="Puntos de control")
#     plt.grid()
#     plt.legend(title="Leyenda", shadow=True, fancybox=True)
#     plt.title(f"Spline $S(x)$")
#     plt.savefig("p5.pdf", transparent=True, bbox_inches="tight")

if __name__ == "__main__":
    # plot()