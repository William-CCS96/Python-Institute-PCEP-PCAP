# ¿Cómo utilizar un tupla?
# Si deseas leer los elementos de una tupla, lo puedes hacer de la misma manera que se hace con las listas.

# Observa el código en el editor.

# El programa debe de generar la siguiente salida, ejecútalo y comprueba:
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
    # 1
    # 1000
    # (10, 100, 1000)
    # (1, 10)        
    # 1
    # 10
    # 100
    # 1000

# Las similitudes pueden ser engañosas - no intentes modificar el contenido de la tupla ¡No es una lista!

# Todas estas instrucciones (con excepción de primera) causarán un error de ejecución :

        # my_tuple = (1, 10, 100, 1000)

        # my_tuple.append(10000)
        # del my_tuple[0]
        # my_tuple[1] = -10
        #AttributeError: 'tuple' object has no attribute 'append'

#   ------------------------------------
# ¿Cómo utilizar una tupla?: continuación
# ¿Qué más pueden hacer las tuplas?

        # La función len() acepta tuplas, y regresa el número de elementos contenidos dentro.
        # El operador + puede unir tuplas (ya se ha mostrado esto antes).
        # El operador * puede multiplicar las tuplas, así como las listas.
        # Los operadores in y not in funcionan de la misma manera que en las listas.
        # El fragmento de código en el editor presenta todo esto.

# La salida es la siguiente:

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
    # 9
    # (1, 10, 100, 1000, 10000)
    # (1, 10, 100, 1, 10, 100, 1, 10, 100)
    # True
    # True


# Una de las propiedades de las tuplas más útiles es que pueden aparecer en el lado izquierdo del operador de asignación. Este fenómeno ya se vio con anterioridad, cuando fue necesario encontrar una manera de intercambiar los valores entre dos variables.

# Observa el siguiente fragmento de código:

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# Muestra tres tuplas interactuando en efecto, los valores almacenados en ellas "circulan" entre ellas. t1 se convierte en t2, t2 se convierte en t3, y t3 se convierte en t1.

# Nota: el ejemplo presenta un importante hecho mas: los elementos de una tupla pueden ser variables, no solo literales. Además, pueden ser expresiones si se encuentran en el lado derecho del operador de asignación.