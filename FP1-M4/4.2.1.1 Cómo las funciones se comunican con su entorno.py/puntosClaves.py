# Puntos Clave
# 1. Se puede pasar información a las funciones utilizando parámetros. Las funciones pueden tener tantos parámetros como sean necesarios.
# Un ejemplo de una función con un parámetro:

def hi(name):
    print("Hola,", name)

hi("Greg")


# Un ejemplo de una función de dos parámetros:

def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)

hi_all("Sebastián", "Konrad")


# Un ejemplo de una función de tres parámetros:

def address(street, city, postal_code):
    print("Tu dirección es:", street, city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")

address(s, c, p_c)


# 2. Puedes pasar argumentos a una función utilizando las siguientes técnicas:

# Paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1).
# Paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2).
# Una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).
#Ejemplo 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # salida: 3
subtra(2, 5)    # salida: -3


#Ejemplo 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # salida: 3
subtra(b=2, a=5)    # salida: 3

#Ejemplo 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # salida: 3
subtra(5, 2)    # salida: 3


# Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave. Es por esa razón que si se intenta ejecutar el siguiente código:

def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # salida: 3
subtra(a=5, 2)    # Syntax Error

# Python no lo ejecutará y marcará un error de sintaxis SyntaxError.

# 3. Se puede utilizar la técnica de argumentos con palabras clave para asignar valores predefinidos a los argumentos:

def name(first_name, last_name="Pérez"):
    print(first_name, last_name)

name("Andy")    # salida: Andy Pérez
name("Bety", "Rodríguez")    # salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")
