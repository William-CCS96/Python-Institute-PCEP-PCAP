"""Excepciones: continuación"""
# Ahora es un buen momento para mostrarte otra instrucción de Python, llamada assert (afirmar). Esta es una palabra clave reservada.
    # assert expression

# ¿Cómo funciona?
        # Se evalúa la expresión.
        # Si la expresión se evalúa como True (Verdadera), o un valor numérico distinto de cero, o una cadena no vacía, o cualquier otro valor diferente de None, no hará nada más.
        # De lo contrario, automáticamente e inmediatamente se genera una excepción llamada AssertionError (en este caso, decimos que la afirmación ha fallado).

# ¿Cómo puede ser utilizada?

        # Puedes ponerlo en la parte del código donde quieras estar absolutamente a salvo de datos incorrectos, y donde no estés absolutamente seguro de que los datos hayan sido examinados cuidadosamente antes (por ejemplo, dentro de una función utilizada por otra persona).
        # El generar una excepción AssertionError asegura que tu código no produzca resultados no válidos y muestra claramente la naturaleza de la falla.
        # Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.

# Si las excepciones y la validación de datos son como conducir con cuidado, la aserción puede desempeñar el papel de una bolsa de aire.

# Veamos a la instrucción assert en acción. Observa el código en el editor. Ejecútalo.

# El programa se ejecuta sin problemas si se ingresa un valor numérico válido mayor o igual a cero; de lo contrario, se detiene y emite el siguiente mensaje:

    # Traceback (most recent call last):
    #   File ".main.py", line 4, in 
    #     assert x >= 0.0
    # AssertionError

import math
x=float(input("Ingresa un número: "))
assert x>=0.0

x=math.sqrt(x)
print(x)