# Puntos Clave

# 1. Puedes emplear la palabra clave reservada return para decirle a una función que devuelva algún valor. La instrucción return termina la función, por ejemplo:

def multiply(a, b):
    return a * b

print(multiply(3, 4))    # salida: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # salida: None


# 2. El resultado de una función se puede asignar fácilmente a una variable, por ejemplo:

def wishes():
    return "¡Felíz Cumpleaños!"

w = wishes()

print(w)    # salida:¡Felíz Cumpleaños!

# Observa la diferencia en la salida en los siguientes dos ejemplos:

# Ejemplo 1
def wishes():
    print("Mis deseos")
    return "Felíz Cumpleaños"

wishes()    # salida: Mis deseos


# Ejemplo 2
def wishes():
    print("Mis deseos")
    return "Felíz Cumpleaños"

print(wishes())

# salida: Mis deseos
#         Felíz Cumpleaños


# 3. Puedes usar una lista como argumento de una función, por ejemplo:

def hi_everybody(my_list):
    for name in my_list:
        print("Hola,", name)

hi_everybody(["Adán", "Juan", "Lucía"])


# 4. Una lista también puede ser un resultado de función, por ejemplo:

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

#-------------------

# Ejercicio 1
# ¿Cuál es la salida del siguiente fragmento de código?

def hi():
    return
    print("¡Hola!")

hi()
# La función devolverá un valor None implícito


# Ejercicio 2
# ¿Cuál es la salida del siguiente fragmento de código?
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
# True
# False
# None

# Ejercicio 3
# ¿Cuál es la salida del siguiente fragmento de código?
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))
# [0, 2, 4, 6, 8, 10]


# Ejercicio 4
# ¿Cuál es la salida del siguiente fragmento de código?

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
# [1, 4, 9, 16, 25]