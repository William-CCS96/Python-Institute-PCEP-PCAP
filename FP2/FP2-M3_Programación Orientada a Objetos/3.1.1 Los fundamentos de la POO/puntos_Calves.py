"""Puntos Clave"""

# 1. Una clase es una idea (más o menos abstracta) que se puede utilizar para crear varias encarnaciones; una encarnación de este tipo se denomina objeto.

# 2. Cuando una clase se deriva de otra clase, su relación se denomina herencia. La clase que deriva de la otra clase se denomina subclase. El segundo lado de esta relación se denomina superclase. Una forma de presentar dicha relación es en un diagrama de herencia, donde:

#     Las superclases siempre se presentan encima de sus subclases.
#     Las relaciones entre clases se muestran como flechas dirigidas desde la subclase hacia su superclase.

# 3. Los objetos están equipados con:

#     Un nombre que los identifica y nos permite distinguirlos.
#     Un conjunto de propiedades (el conjunto puede estar vacío).
#     Un conjunto de métodos (también puede estar vacío).

# 4. Para definir una clase de Python,se necesita usar la palabra clave reservada class. Por ejemplo:

class This_Is_A_Class:
     pass

# 5. Para crear un objeto de la clase previamente definida, se necesita usar la clase como si fuera una función. Por ejemplo:

this_is_an_object = This_Is_A_Class()

