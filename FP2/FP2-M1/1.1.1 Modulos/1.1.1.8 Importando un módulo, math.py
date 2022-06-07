"""Importando un módulo: continuación"""
# Observa el código en el editor. Analízalo cuidadosamente:

from math import sin, pi

print(sin(pi / 2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi / 2))

        # La línea 01: lleva a cabo la importación selectiva.
        # La línea 03: hace uso de las entidades importadas y obtiene el resultado esperado (1.0).
        # La líneas 05 a la 12: redefinen el significado de pi y sin - en efecto, reemplazan las definiciones originales (importadas) dentro del namespace del código.
        # La línea 15: retorna 0.99999999, lo cual confirma nuestras conclusiones.
# Hagamos otra prueba. Observa el código a continuación:

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))

# Aquí, se ha invertido la secuencia de las operaciones del código:

        # Las líneas del 01 al 08: definen nuestro propio pi y sin.
        # La línea 11: hace uso de ellas (0.99999999 aparece en pantalla).
        # La línea 13: lleva a cabo la importación - los símbolos importados reemplazan sus definiciones anteriores dentro del namespace.
        # La línea 15: retorna 1.0 como resultado.
