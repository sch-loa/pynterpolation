from matplotlib import pyplot as plt
from Equation import Expression
import random as rd
import numpy as np
import sympy as sp

from algorithms import polinomio_interpolador_newton, polinomio_interpolador_lagrange
from algorithms import generador_pares_random, grado_polinomio, coeficientes_iguales
from algorithms import newton_mas_secante
from graphics import graficar

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

IGUALDAD_POLINOMIOS_CARTEL = """
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

BUSQUEDA_RAIZ_CARTEL = """
 ____________________________________________________________________________
|                                                                            |
|                     BUSQUEDA DE UNA RAIZ DEL POLINOMIO                     |
|____________________________________________________________________________|
                        """

METODO_LAGRANGE_CARTEL = """
 ____________________________________________________________________________
|                                                                            |
|                     POLINOMIO INTERPOLADOR DE LAGRANGE                     |
|____________________________________________________________________________|
|                                                                            |
|  El método funciona iterativamente. Dado un conjunto de n puntos, el       |
|  polinomio se construye combinando n polinomios base, definidos como:      |
|                                                                            |
|    Ln(x) = (x - x0)(x - x1)...(x - xn) / (xn - x0)(xn - x1)...(xn - xn)    |
|                                                                            |
|  Se destaca que al evaluar Ln(xn) se cancela el término correspondiente    |
|  en la división.                                                           |
|                                                                            |
|  Siendo el polinomio resultante la sumatoria de cada polinomio base,       |
|  multiplicado por la ordenada actual:                                      |
|                                                                            |
|                 P(x) = y0*L0(x) + y1*L1(x) + ... + yn*Ln(x)                |
|____________________________________________________________________________|
                        """

CONCLUSIONES_CARTEL = """
 ____________________________________________________________________________
|                                                                            |
|                                CONCLUSIONES                                |
|____________________________________________________________________________|
|                                                                            |
|  Si bien hay que tener en cuenta que pueden haber errores de redondeo no   |
|  perceptibles en los gráficos debido a diferencias en los cálculos Dado    |
|  un mismo conjunto de datos, tanto el método de Newton como el de          |
|  Lagrange proporcionan exactamente el mismo polinomio interpolador. Lo     |
|  mismo debería pasar si lo comparáramos con el método de diferencias       |
|  divididas. Esto se debe a que el polinomio mínimo que pasa por todos los  |
|  puntos dados es único.                                                    |
|____________________________________________________________________________|
                        """

####################
# METODO DE NEWTON #
####################

# Polinomio interpolador para el conjunto de datos original
pares_xy = generador_pares_random(20)
polinomio, x_simb = polinomio_interpolador_newton(pares_xy)

# Polinomio interpolador para el conjunto de datos invertido
pares_xy_invertidos = pares_xy[::-1]
polinomio_invertido, _ = polinomio_interpolador_newton(pares_xy)

# Polinomio interpolador para el conjunto de datos desordenado aleatoriamente
pares_xy_desordenados = rd.sample(pares_xy, len(pares_xy))
polinomio_desordenado, _ = polinomio_interpolador_newton(pares_xy)

print(METODO_NEWTON_CARTEL)
print(f'   El grado del polinomio es: {grado_polinomio(polinomio)}')
print(IGUALDAD_POLINOMIOS_CARTEL)
if(coeficientes_iguales(polinomio, polinomio_invertido) and coeficientes_iguales(polinomio, polinomio_desordenado)):
    print('   Los coeficientes de los tres polinomios son exactamente iguales.')

# Se busca una raíz con valores iniciales y cota de error de forma arbitraria
print(BUSQUEDA_RAIZ_CARTEL)
x1 = newton_mas_secante(Expression(str(polinomio), ['x']), Expression(str(sp.diff(polinomio)), ['x']), -15, 15, 0.01)
print(f'   La raíz aproximada con dos decimales es {round(x1, 2)}\n')

######################
# METODO DE LAGRANGE #
######################

polinomio_lagrange = polinomio_interpolador_lagrange(pares_xy)

print(METODO_LAGRANGE_CARTEL)
if(coeficientes_iguales(polinomio, polinomio_lagrange)):
    print('   Los coeficientes de los dos polinomios son exactamente iguales.')

print(CONCLUSIONES_CARTEL)

################################################
# GRAFICOS DE LOS POLINOMIOS Y PARES ORDENADOS #
################################################

POLINOMIOS = [polinomio, polinomio_invertido, polinomio_desordenado]
PARES_XY = [pares_xy, pares_xy_invertidos, pares_xy_desordenados]

TITULO_NEWTON = 'Newton vs. Pares {}'
TITULOS = [TITULO_NEWTON.format('Ordenados'), TITULO_NEWTON.format('Invertidos'), TITULO_NEWTON.format('Desordenados')]
COLORES = ['r', 'c', 'y']

# Gráficos del Método de Newton
graficar(POLINOMIOS, PARES_XY, TITULOS, COLORES)

TITULO_LAGRANGE = 'Lagrange vs. Pares Ordenados'
# Gráficos del Método de Lagrange
# (Nota: Este aparece al cerrar todas las ventanas de los graficos anteriores)
graficar([polinomio_lagrange], [pares_xy], [TITULO_LAGRANGE], ['b'])