# La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)
    #1 2 3

#Nombre y apellido, no como en Hungria
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
    # Hola, mi nombre es Luke Skywalker
    # Hola, mi nombre es Jesse Quick
    # Hola, mi nombre es Clark Kent

#Función en Hungría
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
    # Hola, mi nombre es Skywalker Luke
    # Hola, mi nombre es Quick Jesse
    # Hola, mi nombre es Kent Clark
