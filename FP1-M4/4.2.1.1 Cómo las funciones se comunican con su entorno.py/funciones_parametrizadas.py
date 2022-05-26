
# Recuerda que:

    # Los parámetros solo existen dentro de las funciones (este es su entorno natural).
    # Los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.

def message(number,number1):
    print("Ingresa dos números:", number, "y", number1)
message(45,32)

def message2(number):
    print("Ingresa un número:", number)
message2(2)

# Es posible tener una variable con el mismo nombre del parámetro de la función.

def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)

# Modifiquemos la función- ahora tiene dos parámetros:
def function1(what, number):
    print("Ingresa", what, "número", number)
function1("cualquier", 69 )
