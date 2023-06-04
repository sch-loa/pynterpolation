import random
import numpy as np


def polinomio_interpolador_newton(cantidad, metodo):
    pass

def polinomio_interpolador_lagrange(cantidad, metodo):
    pass

def polinomio_interpolador_diferencias_divididas(cantidad, metodo):
    pass

# Genera una lista de n pares aleatorios entre -30 y 30 sin repetición
def generador_pares_random(cantidad):
    num_random = lambda: random.sample(range(-30,30), cantidad)
    return list(zip(num_random(),num_random()))

# Reordena los elementos de uan lista al azar
def reordenar_pares_random(lista):
    return random.shuffle(lista)

def grado_polinomio(polinomio):
    pass