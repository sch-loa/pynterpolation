from matplotlib import pyplot as plt
import random as rd
import numpy as np
import sympy as sp

from algorithms import polinomio_interpolador_newton, generador_pares_random, grado_polinomio, coeficientes_iguales

METODO_NEWTON_CARTEL = """
 ____________________________________________________________________________
|                                                                            |
|                      POLINOMIO INTERPOLADOR DE NEWTON                      |
|____________________________________________________________________________|
|                                                                            |
|  INTEGRANTES:                                                              |
|  |_ Loana Abril Schleich Garcia.                                           |
|____________________________________________________________________________|
|                                                                            |
|                        FUNCIONAMIENTO DEL ALGORITMO                        |
|____________________________________________________________________________|
|                                                                            |
|  El método funciona iterativamente. Dada una lista de pares ordenados se   |
|  la recorre en busca de un polinomio que pase por ese punto y todos los    |
|  anteriores en la colección. En cada iteración se reutiliza el polinomio   |
|  encontrado de forma tal que se le agrege un nuevo punto.                  |
|  Matemáticamente, esto es:                                                 |
|                                                                            |
|   P_n(x) = c0 + c1(x-x_0)+ c2(x-x_0)(x-x_1) + ... + cn(x-x0)...(x-x_n-1)   |
|                                                                            |
|  Siendo n el número de pares ordenados y c el coeficiente de cada factor.  |
|  Cada coeficiente se halla en la corriente iteración agregando los nuevos  |
|  términos y reemplazando los valores (x, y) del actual par ordenado.       |
|                                                                            |
|  Se sabe además que el grado del polinomio es menor o igual al número de   |
|  pares ordenados.                                                          |
|                                                                            |
|  El algoritmo no depende del orden en el que se encuentren los datos,      |
|  esto se verifica interpolando el mismo conjunto de números, invirtiendo   |
|  el orden y cambiándolo aleatoriamente.                                    |
|____________________________________________________________________________|
                    """

IGUALDAD_POLINOMIOS_CARTEL = """\033[F
 ____________________________________________________________________________
|                                                                            |
|                          IGUALDAD ENTRE POLINOMIOS                         |
|____________________________________________________________________________|
|                                                                            |
|  Para comparar la igualdad entre dos polinomios, es posible comparar sus   |
|  coeficientes. Si los coeficientes de los términos correspondientes        |
|  (de esto se presume también que tienen el mismo grado) son idénticos en   |
|  ambos, entonces los mismos son iguales.                                   |
|____________________________________________________________________________|   
                            """

# Polinomio interpolador para el conjunto de datos original
pares_xy = generador_pares_random(20)
polinomio, x_simb = polinomio_interpolador_newton(pares_xy)

# Polinomio interpolador para el conjunto de datos invertido
pares_xy_invertidos = pares_xy[::-1]
polinomio_invertido, x_simb_invertido = polinomio_interpolador_newton(pares_xy)

# Polinomio interpolador para el conjunto de datos desordenado aleatoriamente
pares_xy_desordenados = rd.sample(pares_xy, len(pares_xy))
polinomio_desordenado, x_simb_desordenado = polinomio_interpolador_newton(pares_xy)


PARES_XY = [pares_xy, pares_xy_invertidos, pares_xy_desordenados]
POLINOMIOS = [polinomio, polinomio_invertido, polinomio_desordenado]
X_SIMBS = [x_simb, x_simb_invertido, x_simb_desordenado]

print(METODO_NEWTON_CARTEL)
print(f'   El grado del polinomio es: {grado_polinomio(polinomio)}')
print(IGUALDAD_POLINOMIOS_CARTEL)
if(coeficientes_iguales(polinomio, polinomio_invertido, x_simb) and coeficientes_iguales(polinomio, polinomio_desordenado, x_simb)):
    print('   Los coeficientes de los tres polinomios son exactamente iguales.\n')

# GRAFICOS DE LOS POLINOMIOS Y PARES ORDENADOS
TITULOS = ['Ordenados', 'Invertidos', 'Desordenados']
COLORES = ['r', 'c', 'y']

x = np.linspace(-30, 30, 300)

# Creo un gráfico por cada polinomio
for i in range(len(PARES_XY)):
    func_polinomica = sp.lambdify(X_SIMBS[i], POLINOMIOS[i], 'numpy')
    fig, ax = plt.subplots()

    ax.plot(x, func_polinomica(x), 'k')

    for x_n, y_n in PARES_XY[i]:
        ax.scatter([x_n],[y_n], color = COLORES[i])

    plt.xlim(-18, 18)
    plt.ylim(-18, 18)

    plt.grid(True, linestyle='--', linewidth=0.5, color='gray') 
    plt.title(f'Polinomio Interpolador de Newton vs. Pares {TITULOS[i]}')

plt.show()