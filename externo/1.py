import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol("x")

fx = x**2
n = 2
a = np.zeros(n + 1)
b = np.zeros(n - 1)

## Cálculo de los coeficientes
for k in range(n + 1):
    fkx = sp.cos(k * x) * fx
    a[k] = (1 / np.pi) * sp.integrate(fkx, (x, -sp.pi, sp.pi))

for k in range(1, n):
    gkx = sp.sin(k * x) * fx
    b[k - 1] = (1 / np.pi) * sp.integrate(gkx, (x, -sp.pi, sp.pi))

## Coeficientes
print("Valores de los coeficientes")
for k in range(n + 1):
    print(f"a{k} = {a[k]}")

for k in range(1, n):
    print(f"b{k} = {b[k-1]}")

## Polinomio resultante
print("\nPolinomio resultante")
sum = 0
for k in range(1, n):
    sum += a[k] * sp.cos(k * x) + b[k - 1] * sp.sin(k * x)
S2 = a[0] / 2 + a[n] * sp.cos(n * x) + sum
print(S2)

## Tabla de errores
error = np.zeros(7)
print("\n Tabla de errores")
# Para evaluar varios puntos por medios de un vector tenemos que convertirla a una funcion lambda
px1 = sp.lambdify(x, S2)
px2 = sp.lambdify(x, fx)
for i in range(7):
    error[i] = np.abs(px2(i - 3) - px1(i - 3))
    print(f"X={i-3},f(x)={px2(i-3)},S2(x)={px1(i-3)},error={error[i]}\n")

## Gráfica del polinomio
valx = np.linspace(-np.pi, np.pi, 15)

pfx = px1(valx)  # Evaluacion de los puntos de la abscisa
pfy = px2(valx)  # Evaluacion de los puntos de la ordenada

fig, ax = plt.subplots()
ax.plot(valx, pfx, label="S2(x)")
ax.plot(valx, pfy, label="f(x)")
plt.xlim(-np.pi, np.pi)
plt.legend()

plt.show()


P = np.array([[15, 0, 10], [5, 0, 15], [-5, 0, 15], [-15, 0, 10],
[15, 5, 15], [5, 5, 25], [-5, 5, 25], [-15, 5, 15],
[15, 0, 15], [5, 10, 25], [-5, ]])