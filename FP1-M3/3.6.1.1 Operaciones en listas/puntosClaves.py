# Puntos Clave
# 1. Si tienes una lista list_1, y la siguiente asignación: list_2 = list_1 esto no hace una copia de la lista list_1, pero hace que las variables list_1 y list_2 apunten a la misma lista en la memoria. Por ejemplo:
vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one) # salida: [carro', 'bicicleta', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # elimina 'carro'
print(vehicles_two) # salida: ['bicicleta', 'motor']

# 2. Si deseas copiar una lista o parte de la lista, puedes hacerlo haciendo uso de rebanadas:
colors = ['rojo', 'verde', 'naranja']

copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista

# 3. También puede utilizar índices negativos para hacer uso de rebanadas. Por ejemplo:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']


# 4. Los parámetros start y end son opcionales al partir en rebanadas una lista: list[start:end], por ejemplo:
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # salida: [3, 4, 5]
print(slice_two)  # salida: [1, 2]
print(slice_three)  # salida: [4, 5]

# 5. Puedes eliminar rebanadas utilizando la instrucción del:
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # salida: [3, 4, 5]

del my_list[:]
print(my_list)  # delimina el contenido de la lista, genera: []

# 6. Puedes probar si algunos elementos existen en una lista o no utilizando las palabras clave in y not in, por ejemplo:
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # salida: True
print("C" not in my_list)  # salida: True
print(2 not in my_list)  # salida: False

# Ejercicio 1
# ¿Cuál es la salida del siguiente fragmento de código?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)   
    # ['C']

# Ejercicio 2
# ¿Cuál es la salida del siguiente fragmento de código?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
    #['B', 'C']

# Ejercicio 3
# ¿Cuál es la salida del siguiente fragmento de código?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
    #[]

# Ejercicio 4
# ¿Cuál es la salida del siguiente fragmento de código?

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
    #['A', 'B', 'C']
    

# Ejercicio 5
# Inserta in o not in en lugar de ??? para que el código genere el resultado esperado.

my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # salida True
print("A" not in my_list)  # salida True
print(3 not in my_list)  # salida True
print(False in my_list)  # salida False