# Puntos Clave
"""1. Algunos de los métodos que ofrecen las cadenas son:"""

# capitalize(): cambia todas las letras de la cadena a mayúsculas.
# center(): centra la cadena dentro de una longitud conocida.
# count(): cuenta las ocurrencias de un carácter dado.
# join(): une todos los elementos de una tupla/lista en una cadena.
# lower(): convierte todas las letras de la cadena en minúsculas.
# lstrip(): elimina los caracteres en blanco al principio de la cadena.
# replace(): reemplaza una subcadena dada con otra.
# rfind(): encuentra una subcadena comenzando por el final de la cadena.
# rstrip(): elimina los caracteres en blanco al final de la cadena.
# split(): divide la cadena en una subcadena usando un delimitador dado.
# strip(): elimina los espacios en blanco iniciales y finales.
# swapcase(): intercambia las mayúsculas y minúsculas de las letras.
# title(): hace que la primera letra de cada palabra sea mayúscula.
# upper(): convierte todas las letras de la cadena en letras mayúsculas.

"""2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):"""

# endswith(): ¿La cadena termina con una subcadena determinada?
# isalnum(): ¿La cadena consta solo de letras y dígitos?
# isalpha(): ¿La cadena consta solo de letras?
# islower(): ¿La cadena consta solo de letras minúsculas?
# isspace(): ¿La cadena consta solo de espacios en blanco?
# isupper(): ¿La cadena consta solo de letras mayúsculas?
# startswith(): ¿La cadena consta solo de letras mayúsculas?

#--------------------------
"""Ejercicio 1"""
# ¿Cuál es el resultado esperado del siguiente código?

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

    # ABC123xyz

"""Ejercicio 2"""
# ¿Cuál es el resultado esperado del siguiente código?

s1 = '¿Dónde están las nevadas de antaño?'
s2 = s1.split()
print(s2[-2])
    # de

"""Ejercicio 3"""
# ¿Cuál es el resultado esperado del siguiente código?

the_list = ['¿Dónde', 'están', 'las', 'nevadas?']
s = '*'.join(the_list)
print(s)
    # ¿Dónde*están*las*nevadas?

"""Ejercicio 4"""
# ¿Cuál es el resultado esperado del siguiente código?

s = 'Es fácil o imposible'
s = s.replace('fácil', 'difícil').replace('im', '')
print(s)
    # "Es difícil o posible"
