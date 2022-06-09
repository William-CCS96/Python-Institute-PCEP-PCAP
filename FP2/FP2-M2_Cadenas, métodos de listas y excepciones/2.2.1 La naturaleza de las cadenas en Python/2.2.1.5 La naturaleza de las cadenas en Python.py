# Demostración de la función chr.

print(chr(97))
print(chr(945))

print(chr(ord("a"))=="a")

"""Operaciones con cadenas: chr()"""
# Si conoces el punto de código (número) y deseas obtener el carácter correspondiente, puedes usar la función llamada chr().

# La función toma un punto de código y devuelve su carácter.

# Invocándolo con un argumento inválido (por ejemplo, un punto de código negativo o inválido) provoca las excepciones ValueError o TypeError.

# Ejecuta el código en el editor, su salida es la siguiente:

# a
# α
# salida

# Nota:

# chr(ord(x)) == x
# ord(chr(x)) == x
# De nuevo, realiza tus propios experimentos.


