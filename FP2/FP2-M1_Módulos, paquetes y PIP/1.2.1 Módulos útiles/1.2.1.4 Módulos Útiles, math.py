
"""Funciones seleccionadas del módulo math: continuación"""
# El último grupo consta de algunas funciones de propósito general como:

        # ceil(x) → devuelve el entero más pequeño mayor o igual que x.
        # floor(x) → el entero más grande menor o igual que x.
        # trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
        # factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
        # hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
# Observa el código en el editor. Analiza el programa cuidadosamente.

# Demuestra las diferencias fundamentales entre ceil(), floor() y trunc().
# Ejecuta el programa y verifica su salida.

from math import ceil, factorial, floor, trunc,hypot,sqrt

x = 1.4
y = 2.6

print(floor(x), floor(y))  #1 2
print(floor(-x), floor(-y)) #-2 -3
print(ceil(x), ceil(y))  #2 3
print(ceil(-x), ceil(-y)) #-1 -2
print(trunc(x), trunc(y)) #1 2
print(trunc(-x), trunc(-y)) #-1 -2

print(factorial(5))
print(hypot(1,1))
print(sqrt(pow(1,2)+pow(1,2)))
        # 120
        # 1.4142135623730951
        # 1.4142135623730951


