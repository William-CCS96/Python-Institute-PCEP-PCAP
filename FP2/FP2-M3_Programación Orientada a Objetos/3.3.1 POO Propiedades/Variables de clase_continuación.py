"""Variables de clase: continuación"""
# El cambiar el nombre de una variable de clase tiene los mismos efectos que aquellos con los que ya está familiarizado.

# Mira el ejemplo en el editor. ¿Puedes adivinar su salida?

# Ejecuta el programa y verifica si tus predicciones fueron correctas. Todo funciona como se esperaba, ¿no?

class ExampleClass:
    __counter=0
    def __init__(self, val=1):
        self.__first=val
        ExampleClass.__counter+=1

example_object_1=ExampleClass()
example_object_2=ExampleClass(2)
example_object_3=ExampleClass(4)

print(example_object_1.__dict__,example_object_1._ExampleClass__counter)
print(example_object_2.__dict__,example_object_2._ExampleClass__counter)
print(example_object_3.__dict__,example_object_3._ExampleClass__counter)

    # {'_ExampleClass__first': 1} 3
    # {'_ExampleClass__first': 2} 3
    # {'_ExampleClass__first': 4} 3

print(example_object_1._ExampleClass__first)
# 1