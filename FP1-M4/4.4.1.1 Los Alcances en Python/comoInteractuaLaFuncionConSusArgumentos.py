# El código en el editor nos enseña algo. Como puedes observar, la función cambia el valor de su parámetro. ¿Este cambio afecta el argumento?
def my_function(n):
    print("Yo recibí", n)
    var=n+1
    print("Ahora tengo", n)

var = 1
my_function(var)
print(var)
# Yo recibí 1
# Ahora tengo 2
# 1
    # La conclusión es obvia - al cambiar el valor del parámetro este no se propaga fuera de la función
    # Esto también significa que una función recibe el valor del argumento, no el argumento en sí. Esto es cierto para los valores escalares.

#EJEMPLO 1:
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
    # Print #1: [2, 3]  
    # Print #2: [2, 3]
    # Print #3: [0, 1]  Cambia los valores internos no los de la vaiable externa
    # Print #4: [2, 3]  Toma los valores de la variable externa
    # Print #5: [2, 3]  Toma los valores de la variable externa

#EJEMPLO 2:
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea. Toma es la lista no los parametros
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [3]
# Print #4: [3]
# Print #5: [3]

        #     Intentémoslo:

        # Si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista (Recuerda: las variables que contienen listas son almacenadas de manera diferente que las escalares).
        # Pero si se modifica la lista identificada por el parámetro (Nota: ¡La lista, no el parámetro!), la lista reflejará el cambio.

