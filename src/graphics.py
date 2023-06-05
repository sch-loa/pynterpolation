import sympy as sp
from matplotlib import pyplot as plt
import numpy as np

# Función para gráfico de funciones
def graficar(POLINOMIOS, PARES_XY, TITULOS, COLORES):
    x = np.linspace(-30, 30, 300)
    x_simb = sp.symbols('x')

    for i in range(len(PARES_XY)):
        func_polinomica = sp.lambdify(x_simb, POLINOMIOS[i], 'numpy')
        fig, ax = plt.subplots()

        ax.plot(x, func_polinomica(x), 'k')

        for x_n, y_n in PARES_XY[i]:
            ax.scatter([x_n],[y_n], color = COLORES[i])

        plt.xlim(-18, 18)
        plt.ylim(-18, 18)

        plt.grid(True, linestyle='--', linewidth=0.5, color='gray') 
        plt.title(f'Polinomio Interpolador de {TITULOS[i]}')

    plt.show()