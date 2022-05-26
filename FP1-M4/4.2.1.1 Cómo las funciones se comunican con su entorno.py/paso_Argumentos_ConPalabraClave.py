#el significado del argumento está definido por su nombre, no su posición, a esto se le denomina paso de argumentos con palabra clave.
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
        # Hola, mi nombre es James Bond
        # Hola, mi nombre es Luke Skywalker


#ERROORRR
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
introduction(surname="Skywalker", first_name="Luke")
    # TypeError: introduction() got an unexpected keyword argument 'surname'
    