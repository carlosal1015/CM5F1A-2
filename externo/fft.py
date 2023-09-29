# -*- coding: utf-8 -*-
"""17)TransfFourierDiscreta

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14KO7OUyMG56Qp_3gajh35te7NEnkMn7_
"""

## Renee Jair Lopez Punin

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

x = sp.Symbol("x")
i = sp.Symbol("i")

fx = sp.cos(x) * x**2
n = 4
m = 4
a = np.zeros(m + 1)
b = np.zeros(m - 1)
C_real = np.zeros(m + 1)
C_imag = np.zeros(m + 1)

## Cálculo de los coeficientes
for k in range(m + 1):
    cont_real = 0
    cont_imag = 0
    for j in range(2 * m):
        xj = -np.pi + j * np.pi / 4
        cont_real += fx.subs(x, xj) * np.cos(k * xj)
        cont_imag += fx.subs(x, xj) * np.sin(k * xj)
    C_real[k] = (1 / m) * cont_real
    C_imag[k] = (1 / m) * cont_imag

a = C_real
b = C_imag[1:4]

## Muestra de los coeficientes
print("Los valores de C son:\n")
for k in range(m + 1):
    if k == 0 or k == 4:
        print(f"C{k}={a[k]}")
    else:
        print(f"C{k}={a[k]}+{b[k-1]}i")

print("\nLos valores de a son:\n")
for k in range(m + 1):
    print(f"a{k}={a[k]}")

print("\nLos valores de b son:\n")
for k in range(m - 1):
    print(f"b{k+1}={b[k]}")

## Muestra del polinomio interpolante
print("\nPolinomio interpolante:")
sum = 0
for k in range(1, m):
    sum += a[k] * sp.cos(k * x) + b[k - 1] * sp.sin(k * x)
S4 = (a[0] + a[n] * sp.cos(n * x)) / 2 + sum
print(S4)

## Tabla de errores
error = np.zeros(9)
print("\n Tabla de errores")
# Para evaluar varios puntos por medios de un vector tenemos que convertirla a una funcion lambda
px1 = sp.lambdify(x, S4)
px2 = sp.lambdify(x, fx)
for i in range(9):
    error[i] = np.abs(px2(-np.pi + np.pi / (i + 1)) - px1(-np.pi + np.pi / (i + 1)))
    print(
        f"X_({i-9})={-np.pi+np.pi/(i+1)}, f(xi)={px2(-np.pi+np.pi/(i+1))}, S4(x)={px1(-np.pi+np.pi/(i+1))}, error={error[i]}\n"
    )
for i in range(9):
    error[i] = np.abs(
        px2(2 * np.pi - 2 * np.pi / (i + 1)) - px1(2 * np.pi - 2 * np.pi / (i + 1))
    )
    print(
        f"X_({i})={np.pi-np.pi/(i+1)}, f(xi)={px2(np.pi-np.pi/(i+1))}, S4(x)={px1(np.pi-np.pi/(i+1))}, error={error[i]}\n"
    )

## Gráfica del polinomio
valx = np.linspace(-np.pi, np.pi, 50)

pfx = px1(valx)  # Evaluacion de los puntos de la abscisa
pfy = px2(valx)  # Evaluacion de los puntos de la ordenada


fig, ax = plt.subplots()
ax.plot(valx, pfx, label="S4(x)")
ax.plot(valx, pfy, label="f(x)")
plt.xlim(-np.pi, np.pi)
plt.legend()

plt.show()