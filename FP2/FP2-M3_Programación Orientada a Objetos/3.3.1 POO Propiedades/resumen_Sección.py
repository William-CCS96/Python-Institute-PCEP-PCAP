"""Puntos Clave"""

# 1. Una variable de instancia es una propiedad cuya existencia depende de la creación de un objeto. Cada objeto puede tener un conjunto diferente de variables de instancia.

# Además, se pueden agregar y quitar libremente de los objetos durante su vida útil. Todas las variables de instancia de objeto se almacenan dentro de un diccionario dedicado llamado __dict__, contenido en cada objeto por separado.


# 2. Una variable de instancia puede ser privada cuando su nombre comienza con __, pero no olvides que dicha propiedad aún es accesible desde fuera de la clase usando un nombre modificado construido como < codel>_ClassName__PrivatePropertyName.

class ExampleClass:
    __variable=5
    def __init__(self):
        self.__var=1

example_object=ExampleClass()

print(ExampleClass._ExampleClass__variable)#Variable de clase  5
print(example_object._ExampleClass__var)#Variable de instancia  1
    
# 3. Una variable de clase es una propiedad que existe exactamente en una copia y no necesita ningún objeto creado para ser accesible. Estas variables no se muestran como contenido de __dict__.

# Todas las variables de clase de una clase se almacenan dentro de un diccionario dedicado llamado __dict__, contenido en cada clase por separado.


# 4. Una función llamada hasattr() se puede utilizar para determinar si algún objeto o clase contiene cierta propiedad especificada.

class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Variable de instancia.
        self.__delta = 3 # Variable de instancia privada.


obj = Sample()
obj.beta = 2  # Otra variable de instancia (que existe solo dentro de la instancia "obj").
print(obj.__dict__)
        # {'alpha': 1, '_Sample__delta': 3, 'beta': 2}


#-----------------------------
"""Ejercicio 1"""
# ¿Cuáles de las propiedades de la clase Python son variables de instancia y cuáles son variables de clase? ¿Cuáles de ellos son privados?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False

    # population y victims son variables de clase, mientras que length y __venomous son variables de instancia (esta última también es privada)

"""Ejercicio 2"""
# Vas a negar la propiedad __venomous del objeto version_2, ignorando el hecho de que la propiedad es privada. ¿Cómo vas a hacer esto?

class Python:
    def __init__(self):
        self.__venomous=True

version_2=Python()

version_2._Python__venomous= not version_2._Python__venomous
print(version_2.__dict__)

"""Ejercicio 3"""
# Escribe una expresión que compruebe si el objeto version_2 contiene una propiedad de instancia denominada constrictor (¡si, constrictor!).

if hasattr(version_2,"constrictor"):
    print(version_2.constrictor)
else:
    print("!No, constrictor¡")


