"""Puntos Claves"""

# 1. Las cadenas de Python son secuencias inmutables y se pueden indexar, dividir en rebanadas e iterar como cualquier otra secuencia, además de estar sujetas a los operadores in y not in. Existen dos tipos de cadenas en Python:

# Cadenas de una línea, las cuales no pueden cruzar los límites de una línea, las denotamos usando apóstrofes ('cadena') o comillas ("cadena").
# Cadenas multilínea, que ocupan más de una línea de código fuente, delimitadas por apóstrofes triples:

'''
cadena
'''
o
"""
cadena
"""
# 2. La longitud de una cadena está determinada por la función len(). El carácter de escape (\) no es contado. Por ejemplo:
print(len("\n\n"))
# Susalida es 2.

# 3. Las cadenas pueden ser concatenadas usando el operador +, y replicadas usando el operador *. Por ejemplo:

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)
# *+*+*+*+*.

# 4. El par de funciones chr() y ord() se pueden utilizar para crear un carácter utilizando su punto de código y para determinar un punto de código correspondiente a un carácter. Las dos expresiones siguientes son siempre verdaderas:

chr(ord(character)) == character
ord(chr(codepoint)) == codepoint

# 5. Algunas otras funciones que se pueden aplicar a cadenas son:

list()  # crea una lista que consta de todos los caracteres de la cadena.
max() # encuentra el carácter con el punto de código máximo.
min() # encuentra el carácter con el punto de código mínimo.

# 6. El método llamado index() encuentra el índice de una subcadena dada dentro de la cadena.

"""Ejercicio 1"""
# ¿Cuál es la longitud de la siguiente cadena asumiendo que no hay espacios en blanco entre las comillas?

"""
"""
    # 1

"""Ejercicio 2"""
# ¿Cuál es el resultado esperado del siguiente código?

s = 'yesteryears'
the_list = list(s)
print(the_list[3:6])
    # ['t', 'e', 'r']

"""Ejercicio 3"""
# ¿Cuál es el resultado esperado del siguiente código?

for ch in "abc":
    print(chr(ord(ch) + 1), end='')
    # bcd