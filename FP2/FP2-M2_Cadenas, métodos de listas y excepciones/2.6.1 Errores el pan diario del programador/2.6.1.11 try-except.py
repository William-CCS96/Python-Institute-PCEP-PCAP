"""Excepciones: continuación"""
# Echemos a perder el código una vez más.

# Observa el programa en el editor. Esta vez, hemos eliminado el bloque sin nombre.
try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")

# El usuario ingresa nuevamente un 0, y:

    # La excepción no será manejada por ValueError: no tiene nada que ver con ello.
    # Como no hay otro bloque, deberías ver este mensaje:

# Traceback (most recent call last):
# File "exc.py", line 3, in 
# y = 1 / x
# ZeroDivisionError: division by zero

# Has aprendido mucho sobre el manejo de excepciones en Python. En la siguiente sección, nos centraremos en las excepciones integradas de Python y sus jerarquías.

