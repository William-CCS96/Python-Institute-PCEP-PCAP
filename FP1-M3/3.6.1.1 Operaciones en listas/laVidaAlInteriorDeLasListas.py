list_1 = [1]
list_2 = list_1
list_1[0] = 2
del list_2[0]
print(list_1)


# Se podría decir que:

# El nombre de una variable ordinaria es el nombre de su contenido.
# El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.

# La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. En efecto, los dos nombres (list_1 y list_2) identifican la misma ubicación en la memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa.