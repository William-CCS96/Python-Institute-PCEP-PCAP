#VALORES PREDEFINIDOS
# El valor por default para el parámetro se asigna de la siguiente manera:

def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction("William")
    #Hola, mi nombre es William González
introduction("Jorge", "Pérez")
    # Hola, mi nombre es Jorge Pérez}

def introduction2(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)
introduction2()
    # Hola, mi nombre es Juan González
introduction2(last_name="Rodríguez")
    # Hola, mi nombre es Juan Rodríguez
    