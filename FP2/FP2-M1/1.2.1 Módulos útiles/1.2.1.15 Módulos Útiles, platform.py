
"""Funciones seleccionadas del módulo platform: continuación"""
# Las funciones python_implementation y python_version_tuple

# Si necesitas saber que versión de Python está ejecutando tu código, puedes verificarlo utilizando una serie de funciones dedicadas, aquí hay dos de ellas:

        # python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
        # python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
                # La parte mayor de la versión de Python.
                # La parte menor.
                # El número del nivel de parche.

# Nuestro programa de ejemplo produjo el siguiente resultado:
    # CPython
    # 3
    # 7
    # 7

from platform import python_implementation,python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

    # CPython
    # 3
    # 10
    # 4