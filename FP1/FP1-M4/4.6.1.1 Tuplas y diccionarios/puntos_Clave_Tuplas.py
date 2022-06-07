# Puntos Clave: Tuplas
# 1. Las Tuplas son colecciones de datos ordenadas e inmutables. Se puede pensar en ellas como listas inmutables. Se definen con paréntesis:

my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)
    # (1, 2, True, 'una cadena', (3, 4), [5, 6], None)

my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)
    # [1, 2, True, 'una cadena', (3, 4), [5, 6], None]
#---------------------------
# 2. Se puede crear una tupla vacía de la siguiente manera:
empty_tuple = ()
print(type(empty_tuple))    
    # salida: <class 'tuple'>

#--------------------------
# 3. La tupla de un solo elemento se define de la siguiente manera:
one_elem_tuple_1 = ("uno", )    # Paréntesis y una coma.
one_elem_tuple_2 = "uno",       # Sin paréntesis, solo la coma.

    # Si se elimina la coma, Python creará una variable no una tupla:
my_tuple_1 = 1, 
print(type(my_tuple_1))    # salida: <class 'tuple'>

my_tuple_2 = 1             # Esto no es una tupla.
print(type(my_tuple_2))    # salida: <class 'int'>

#--------------------------
# 4. Se pueden acceder los elementos de la tupla al indexarlos: 
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(my_tuple[3])    # salida: [3, 4]
#--------------------------
# 5. Las tuplas son immutable, lo que significa que no se puede agregar, modificar, cambiar o quitar elementos. El siguiente fragmento de código provocará una excepción:
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
my_tuple[2] = "guitarra"    # La excepción TypeError será lanzada.
    # Sin embargo, se puede eliminar la tupla completa:
my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple)  # NameError: name 'my_tuple' is not defined

#---------------------------
# 6. Puedes iterar a través de los elementos de una tupla con un bucle (Ejemplo 1), verificar si un elemento o no esta presente en la tupla (Ejemplo 2), emplear la función len() para verificar cuantos elementos existen en la tupla (Ejemplo 3), o incluso unir o multiplicar tuplas (Ejemplo 4):

# Ejemplo 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
    # 1
    # 2
    # 3
# Ejemplo 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
    # False
    # True
# Ejemplo 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))
    # 4
# Ejemplo 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)
    # (1, 2, 3, 1, 2, 3, 4)
    # (1, 2, 3, 5, 1, 2, 3, 5)

#--------------------------
# También se puede crear una tupla utiliz,o la función integrada de Python tuple(). Esto es particularmente útil cu,o se desea convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla:
my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # salida: [2, 4, 6]
print(type(my_list))    # salida: <class 'list'>
tup = tuple(my_list)
print(tup)    # salida: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>
print(my_list)
#--------------------------
# De la misma manera, cu,o se desea convertir un iterable en una lista, se puede emplear la función integrada de Python denominada list():
tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # salida: <class 'list'>





