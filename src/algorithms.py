import random
import numpy as np
from sympy import symbols, Eq, Poly, solve


def polinomio_interpolador_newton(pares_xy):
    x = symbols('x')
    c = symbols('c')

    p_factores = factor_polinomio(pares_xy)

    _, y0 = pares_xy[0]
    p0 = y0
    for x1, y1 in pares_xy[1:]:
        p1 = p0 + c * next(p_factores)
        c_1 = calcular_coeficiente(p1, (x1, y1), (x, c))
        p1 = p1.replace(c, c_1)

        p0 = p1

    return (p0, x)


def polinomio_interpolador_lagrange():
    pass

def polinomio_interpolador_diferencias_divididas():
    pass

# Calcula el coeficiente del polinomio reemplazando el valor
# de la variable simbólica x y despejando c
def calcular_coeficiente(p1, valores, simbolos):
    x1, y1 = valores
    x, c = simbolos
    return solve(Eq(p1, y1).subs(x, x1), c)[0]

# Dada una lista de numeros x_n retorna la multiplicación de los primeros n elementos
# en su forma (x - x_n), con n creciendo en cada iteración, es decir:
# Primera iteración: (x - x_0)
# Segunda iteración: (x - x_0)*(x - x_1)
# N-nésima iteración: (x - x_0)*(x - x_1)*(x - x_2)...*(x - x_n)
def factor_polinomio(pares_xy):
    x = symbols('x')
    factores_xy = 1
    for x0, _ in pares_xy:
        factores_xy *= x - x0
        yield factores_xy

# Genera una lista de n pares aleatorios entre -15 y 15 sin repetición
def generador_pares_random(cantidad):
    num_random = lambda: random.sample(range(-15,15), cantidad)
    return list(zip(num_random(),num_random()))

def grado_polinomio(polinomio):
    return Poly(polinomio).degree()

# Compara los coeficientes de una lista de polinomios entre sí
def coeficientes_iguales(p0, p1, x):
    return Poly(p0, x).all_coeffs() == Poly(p1, x).all_coeffs()