"""Las cadenas de Python son inmutables"""
# También te hemos dicho que las cadenas de Python son inmutables. Esta es una característica muy importante. ¿Qué significa?

# Esto significa principalmente que la similitud de cadenas y listas es limitada. No todo lo que puede hacerse con una lista puede hacerse con una cadena.

# La primera diferencia importante no te permite usar la instrucción del para eliminar cualquier cosa de una cadena.

# El ejemplo siguiente no funcionará:

alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]

# Lo único que puedes hacer con del y una cadena es eliminar la cadena como un todo. Intenta hacerlo.
# Las cadenas de Python no tienen el método append() - no se pueden expander de ninguna manera.
# El siguiente ejemplo es erróneo:

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")

# Con la ausencia del método append(), el método insert() también es ilegal:
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")