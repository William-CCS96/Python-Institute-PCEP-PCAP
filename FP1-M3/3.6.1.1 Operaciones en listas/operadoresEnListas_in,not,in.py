# Los operadores in y not in
# Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.

    # Estos operadores son:

    # elem in my_list
    # elem not in my_list

    # El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el operador devuelve True en este caso.

    # El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso.

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
    # False
    # True
    # True
print("\n",5 in my_list or 3 in my_list) 
    # True
    