"""Variables de instancia: continuación"""

# Observa el ejemplo modificado en el editor.

# Es casi lo mismo que el anterior. La única diferencia está en los nombres de las propiedades. Hemos antepuesto dos guiones bajos (__).

# Como sabes, tal adición hace que la variable de instancia sea privada, se vuelve inaccesible desde el mundo exterior.

# El comportamiento real de estos nombres es un poco más complicado, así que ejecutemos el programa. Esta es la salida:
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

# Prueba
# del example_object_2._ExampleClass__first
# del example_object_3.__third

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

"""{'_ExampleClass__first': 1}
{'_ExampleClass__first': 2, '_ExampleClass__second': 3}
{'_ExampleClass__first': 4, '__third': 5}"""

# Prueba
"""{'_ExampleClass__first': 1}
{'_ExampleClass__second': 3}
{'_ExampleClass__first': 4}"""

# ¿Puedes ver estos nombres extraños llenos de guiones bajos? ¿De dónde provienen?

# Cuando Python ve que deseas agregar una variable de instancia a un objeto y lo vas a hacer dentro de cualquiera de los métodos del objeto, maneja la operación de la siguiente manera:

"""
    Coloca un nombre de clase antes de tu nombre.
    Coloca un guión bajo adicional al principio."""

"Es por ello que __first se convierte en _ExampleClass__first."

# Obtendrás un resultado válido sin errores ni excepciones.

# Como puedes ver, hacer que una propiedad sea privada es limitado.

# No funcionará si agregas una variable de instancia fuera del código de la clase. En este caso, se comportará como cualquier otra propiedad ordinaria.

