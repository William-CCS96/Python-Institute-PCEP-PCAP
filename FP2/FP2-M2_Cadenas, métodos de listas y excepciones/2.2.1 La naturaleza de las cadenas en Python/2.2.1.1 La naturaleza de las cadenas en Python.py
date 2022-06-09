
# Cadenas: una breve reseña
# Hagamos un breve repaso de la naturaleza de las cadenas en Python.

# En primer lugar, las cadenas de Python (o simplemente cadenas, ya que no vamos a discutir las cadenas de ningún otro lenguaje) son secuencias inmutables.

# Es muy importante tener en cuenta esto, porque significa que debes esperar un comportamiento familiar.

# Analicemos el código en el editor para entender de lo qué estamos hablando:

# Observa el Ejemplo 1. La función len() empleada en las cadenas devuelve el número de caracteres que contiene el argumento. La salida del código es 2.
# Cualquier cadena puede estar vacía. Si es el caso, su longitud es 0 como en el Ejemplo 2.

# No olvides que la diagonal invertida (\) empleada como un carácter de escape, no esta incluida en la longitud total de la cadena. El código en el Ejemplo 3, da como salida un 3.
# Ejecuta los tres ejemplos de código y verifícalo.


# Ejemplo 1
word = 'by'
print(len(word))
    # 2

# Ejemplo 2
empty = ''
print(len(empty))
    # 3

# Ejemplo 3
i_am = 'I\'m'
print(len(i_am))
    # 0