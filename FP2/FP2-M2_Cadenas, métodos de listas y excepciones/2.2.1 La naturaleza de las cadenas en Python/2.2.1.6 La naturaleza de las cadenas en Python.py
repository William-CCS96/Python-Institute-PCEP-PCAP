the_str="William Correa"

for i in range(len(the_str)):
    print(the_str[i], end=" ")
    # W i l l i a m   C o r r e a 
print()
for i in the_str:
    print(i,end="")
    # William Correa

"""Cadenas como secuencias: indexación"""
# Ya dijimos antes que las cadenas de Python son secuencias. Es hora de mostrarte lo que significa realmente.
# Las cadenas no son listas, pero pueden ser tratadas como tal en muchos casos.
# Por ejemplo, si deseas acceder a cualquiera de los caracteres de una cadena, puedes hacerlo usando indexación. Ejecuta el programa:

# Indexando cadenas.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()


# Ten cuidado, no intentes pasar los límites de la cadena, ya que provocará una excepción.
# La salida del ejemplo es:

# s i l l y   w a l k s


# Por cierto, los índices negativos también se comportan como se espera. Comprueba esto tú mismo.


# Cadenas como secuencias: iterando
# El iterar a través de las cadenas funciona también. Observa el siguiente ejemplo:

# Iterando a través de una cadena.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()
# La salida es la misma que el ejemplo anterior. Revísalo.