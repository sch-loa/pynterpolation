from matplotlib import pyplot as plt
import random as rd
import numpy as np
import sympy as sp

from algorithms import polinomio_interpolador_newton

pares_xy, polinomio, x_simb = polinomio_interpolador_newton()

pares_xy_invertidos = pares_xy[::-1]
pares_xy_desordenados = rd.sample(pares_xy, len(pares_xy))

# GRAFICOS DE LOS POLINOMIOS Y PARES ORDENADOS
func_polinomica = sp.lambdify(x_simb, polinomio, 'numpy')
fig, ax = plt.subplots()

x = np.linspace(-30, 30, 300)
ax.plot(x, func_polinomica(x), 'k')

for x_n, y_n in pares_xy:
    ax.scatter([x_n],[y_n], color='r')


plt.xlim(-18, 18)
plt.ylim(-18, 18)

plt.grid(True, linestyle='--', linewidth=0.5, color='gray') 
plt.title('Polinomio Interpolador de Newton vs. Pares Ordenados')

plt.show()