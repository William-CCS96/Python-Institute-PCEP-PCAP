
str1="a"
str2="b"

print(str1+str2)
print(5*str1)
print(str2*4)
str1+=str2
print(str1)

"""Operaciones con cadenas"""
# Al igual que otros tipos de datos, las cadenas tienen su propio conjunto de operaciones permitidas, aunque son bastante limitadas en comparación con los números.

# En general, las cadenas pueden ser:

# Concatenadas (unidas).
# Replicadas.
# La primera operación la realiza el operador + (toma en cuenta que no es una adición o suma) mientras que la segunda por el operador * (toma en cuenta de nuevo que no es una multiplicación).

# La capacidad de usar el mismo operador en tipos de datos completamente diferentes (como números o cadenas) se llama overloading - sobrecarga (debido a que el operador está sobrecargado con diferentes tareas).

# Analiza el ejemplo:

# El operador + es empleado en dos o más cadenas y produce una nueva cadena que contiene todos los caracteres de sus argumentos (nota: el orden es relevante aquí, en contraste con su versión numérica, la cual es conmutativa).
# El operador * necesita una cadena y un número como argumentos; en este caso, el orden no importa: puedes poner el número antes de la cadena, o viceversa, el resultado será el mismo: una nueva cadena creada por la enésima replicación de la cadena del argumento.
# El fragmento de código produce el siguiente resultado:

# ab
# ba
# aaaaa
# bbbb
# salida


# Nota: Los atajos de los operadores anteriores también son aplicables para las cadenas (+= y *=).

