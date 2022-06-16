"""Errores, fallas y otras plagas"""
# Cualquier cosa que pueda salir mal, saldrá mal.
# Esta es la ley de Murphy, y funciona en todo y siempre. Si la ejecución del código puede salir mal, lo hará.

# Observa el código en el editor. Hay al menos dos formas posibles de que "salga mal" la ejecución. ¿Puedes verlas?
import math

x = float(input("Ingresa x: "))
y = math.sqrt(x)

print("La raíz cuadrada de", x, "es igual a", y)


        # Como el usuario puede ingresar una cadena de caracteres completamente arbitraria, no hay garantía de que la cadena se pueda convertir en un valor flotante: esta es la primera vulnerabilidad del código.
        # La segunda es que la función sqrt() fallará si se le ingresa un valor negativo.

# Puedes recibir alguno de los siguientes mensajes de error.
# Algo como esto:

# Ingresa x: Abracadabra
# Traceback (most recent call last):
#   File "sqrt.py", line 3, in <module>
#     x = float(input("Ingresa x: "))
# ValueError: could not convert string to float: 'Abracadabra'

# O algo como esto:
# Ingresa x: -1
# Traceback (most recent call last):
#   File "sqrt.py", line 4, in <module>
#     y = math.sqrt(x)
# ValueError: math domain error

# ¿Puedes protegerte de tales sorpresas? Por supuesto. Además, tienes que hacerlo para ser considerado un buen programador.
