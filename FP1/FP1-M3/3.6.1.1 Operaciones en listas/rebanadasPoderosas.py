# Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Una de las formas más generales de la rebanada es la siguiente:
    # my_list[start:end]
        # start es el índice del primer elemento incluido en la rebanada.
        # end es el índice del primer elemento no incluido en la rebanada.

# Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen: los elementos de los índices desde el principio hasta el fin - 1.
    # Nota: no hasta el fin, sino hasta fin-1. Un elemento con un índice igual a fin es el primer elemento el cual no participa en la segmentación.
    # Es posible utilizar valores negativos tanto para el inicio como para el fin(al igual que en la indexación).

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-3:-1]
print(new_list)
    # [6, 4]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:5] #La lista new_list contendrá fin - inicio (3 - 1 = 2) elementos â los que tienen índices iguales a 1 y 2 (pero no 3).
print(new_list)
    # [8, 6, 4, 2]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
    # [8, 6, 4]

# Si start especifica un elemento que se encuentra más allá del descrito por end (desde el punto de vista inicial de la lista), la rebanada estará vacía:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list) 
    # []

# Si omites el start en tu rebanada, se supone que deseas obtener un segmento que comienza en el elemento con índice 0.
# En otras palabras, la rebanada sería de esta forma:
    # my_list[:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
    #[10, 8, 6]

# Del mismo modo, si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice len(my_list)
    # my_list[start:]
# es un equivalente más compacto de:
    # my_list[start:len(my_list)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
    # [4, 2]

#REBANADAS Y del

# La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez, también puede eliminar rebanadas:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
    # [10, 4, 2]

# También es posible eliminar todos los elementos a la vez:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
    # []

# La instrucción del eliminará la lista, no su contenido.
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
    # NameError: name 'my_list' is not defined. Did you mean: 'new_list'?
    




