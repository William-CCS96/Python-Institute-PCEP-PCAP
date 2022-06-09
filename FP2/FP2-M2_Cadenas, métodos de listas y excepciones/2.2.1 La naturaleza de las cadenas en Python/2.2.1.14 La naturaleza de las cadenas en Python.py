"""Operaciones con cadenas: la función list()"""
# La función list() toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena, uno por elemento de la lista.

# Nota: no es estrictamente una función de cadenas - list() es capaz de crear una nueva lista de muchas otras entidades (por ejemplo, de tuplas y diccionarios).


"""Operaciones con cadenas: el método count()"""
# El método count() cuenta todas las apariciones del elemento dentro de la secuencia. La ausencia de tal elemento no causa ningún problema.
# Observa el segundo ejemplo en el editor. ¿Puedes adivinar su salida?


# Las cadenas de Python tienen un número significativo de métodos destinados exclusivamente al procesamiento de caracteres. No esperes que trabajen con otras colecciones. La lista completa se presenta aquí: https://docs.python.org/3.4/library/stdtypes.html#string-methods.
# Te mostraremos los que consideramos más útiles.


# Demostración de la función list():
print(list("abcabc"))
    # ['a', 'b', 'c', 'a', 'b', 'c']

# Demostración de la función list():
print("abcabc".count("b"))
print('abcabc'.count("d"))
    # 2
    # 0
    