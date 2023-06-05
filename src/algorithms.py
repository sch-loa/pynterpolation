import random
import numpy as np
from sympy import symbols, Eq, Poly, solve

# Función principal del método de newton
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


def polinomio_interpolador_lagrange(pares_xy):
    x = symbols('x')

    # Tomo el último valor del generador
    factor_xy = 0
    for factor in factor_polinomio(pares_xy):
        factor_xy = factor
    
    polinomio = 0
    for x1, y1 in pares_xy:
        l1_factor = factor_xy / (x - x1) # Cancelo el par actual
        l1 = y1 *(l1_factor / l1_factor.replace(x, x1))
        polinomio += l1
 
    return polinomio

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


#################################################
# FUNCIONES PARA APROXIMAR RAÍCES (TP ANTERIOR) #
#################################################

# Se sacaron funcionalidades innecesarias como el manejo de los datos
# utilizados en cada iteración, ya que solo nos interesa hallar la raíz.

# Combina los algoritmos de la secante y newton-raphson
def newton_mas_secante(fx, fxp, x0, x1, err):
    c = 1 # Contador de la iteración
    condicion = lambda p0, p1 : error_absoluto(p0,p1) < err or error_absoluto(p0,p1) == 0 or fx(p0) == 0 or fx(p1) == 0 # Condicion de parada
    while(not condicion(x0,x1)):
        x0, x1 = secante(fx, x0, x1) # Recibe datos actualizados y nuevo x0, x1
        c += 1

        # Verifica la condición para el cálculo anterior
        if(condicion(x0,x1)):
            break
        
        x0, x1 = newtonraphson(fx,fxp,x1) # Recibe datos actualizados y nuevo x0, x1
        c += 1

    return x1

def newtonraphson(fx,fxp,p0):
    p1 = p0 - (fx(p0))/fxp(p0)
    return (p0, p1)

def secante(fx,p0,p1):
    dividendo = fx(p1) - fx(p0)

    # Para evitar una división por cero se le suma una cantidad mínima al dividendo
    # en caso de ser cero para evitar errores pero a la vez no perjudicar el cálculo.
    if(dividendo == 0):
        dividendo = 10**-10

    p2 = p1 - (fx(p1)*(p1-p0)) / dividendo

    return (p1,p2)

def error_absoluto(x0, x1):
    return abs(x1 - x0)