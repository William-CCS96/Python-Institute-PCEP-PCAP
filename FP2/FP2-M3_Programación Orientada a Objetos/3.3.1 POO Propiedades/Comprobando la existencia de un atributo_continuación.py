"""Comprobando la existencia de un atributo: continuación"""
# La instrucción try-except te brinda la oportunidad de evitar problemas con propiedades inexistentes.

# Es fácil: mira el código en el editor.

# Como puedes ver, esta acción no es muy sofisticada. Esencialmente, acabamos de barrer el tema debajo de la alfombra.

# Afortunadamente, hay una forma más de hacer frente al problema.

class ExampleClass:
    def __init__(self,val):
        if val%2!=0:
            self.a=1
        else:
            self.b=2

example_object=ExampleClass(5)

print(example_object.a)
try:
    print(example_object.b)
except AttributeError:
    pass

"""Afortunadamente, hay una forma más de hacer frente al problema."""

# Python proporciona una función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica. La función se llama hasattr, y espera que le pasen dos argumentos:

        # La clase o el objeto que se verifica.
        # El nombre de la propiedad cuya existencia se debe informar (Nota: debe ser una cadena que contenga el nombre del atributo).

# La función retorna True o False.

print(hasattr(example_object,"b"))
print(hasattr(example_object,"a"))

if hasattr(example_object,"b"):
    print(example_object.b)
else:
    print("El objeto no posee esa propiedad")

        # 1
        # False
        # True
        # El objeto no posee esa propiedad

"""No olvides que la función hasattr() también puede operar en clases. Puedes usarla para averiguar si una variable de clase está disponible, como en el ejemplo en el editor."""

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

    # True
    # False

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'c'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

    # True
    # False
    # False
    # True