"""Funciones seleccionadas del módulo random: continuación"""
# Las funciones randrange y randint

# Si deseas valores aleatorios enteros, una de las siguientes funciones encajaría mejor:

        # randrange(fin)
        # randrange(inico, fin)
        # randrange(inicio, fin, incremento)
        # randint(izquierda, derecha)
# Las primeras tres invocaciones generarán un valor entero tomado (pseudoaleatoriamente) del rango:

        # range(fin)
        # range(inicio, fin)
        # range(inicio, fin, incremento)
# Toma en cuenta la exclusión implícita del lado derecho.

# La última función es equivalente a randrange(izquierda, derecha+1) - genera el valor entero i, el cual cae en el rango [izquierda, derecha] (sin exclusión en el lado derecho).

# Observa el código en el editor. Este programa generará una línea que consta de tres ceros y un cero o un uno en el cuarto lugar.

from random import randrange, randint

print(randrange(10), end=' ')
print(randrange(0, 5), end=' ')
print(randrange(0, 10, 1), end=' ')
print(randint(0, 1))

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

