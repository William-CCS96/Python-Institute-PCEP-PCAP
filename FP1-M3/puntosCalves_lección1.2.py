Puntos Clave

1. Existen dos tipos de bucles en Python: while y for:

El bucle while ejecuta una sentencia o un conjunto de sentencias siempre que una condición booleana especificada sea verdadera, por ejemplo:

# Ejemplo 1
while True:
    print("Atascado en un bucle infinito.")

# Ejemplo 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1


El bucle for ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia (por ejemplo, una lista, un diccionario, una tupla o un conjunto; pronto aprenderás sobre ellos) u otros objetos que son iterables (por ejemplo, cadenas). Puedes usar el bucle for para iterar sobre una secuencia de números usando la función incorporada range. Mira los ejemplos a continuación:

# Ejemplo 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Ejemplo 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)


2. Puedes usar las sentencias break y continue para cambiar el flujo de un bucle:

Utiliza break para salir de un bucle, por ejemplo:

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")


Utiliza continue para omitir la iteración actual, y continuar con la siguiente iteración, por ejemplo:

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
