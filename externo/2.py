import matplotlib.pyplot as plt
import numpy as np

m = 4


def f(x):
    return np.exp(x) * np.cos(x)


x = np.array([-np.pi + (np.pi * i / m) for i in np.arange(0, 2 * m)])
y = f(x)


def S(t, n):
    a = np.zeros(n + 1)
    b = np.zeros(n + 1)
    for i in np.arange(0, n + 1):
        a[i] = np.sum([y[j] * np.cos(i * x[j]) for j in np.arange(0, 2 * m)]) / m
        if i != 0 and i != n:
            b[i] = np.sum([y[j] * np.sin(i * x[j]) for j in np.arange(0, 2 * m)]) / m
    s = +(a[0] / 2) + a[n] * np.cos(n * t)
    for i in np.arange(1, n):
        s = s + a[i] * np.cos(i * t) + b[i] * np.sin(i * t)
    return s

print(x)
k = 1
print(np.cos(k * x))
# np.cos(k * x)
# print(np.sum(np.cos(k * x)))
# t = np.linspace(-np.pi, np.pi, num=1000)
# w = f(t)
# z = S(t, 2)
# plt.plot(t, w, "red", label="f(x)")
# plt.plot(t, z, "blue", label="$S_2(x)$")

# plt.plot(x, y, "ro")

# plt.legend(loc="upper left")
# plt.show()
