"""Comprobando la existencia de un atributo"""
# La actitud de Python hacia la instanciación de objetos plantea una cuestión importante: en contraste con otros lenguajes de programación, es posible que no esperes que todos los objetos de la misma clase tengan los mismos conjuntos de propiedades.

# Justo como en el ejemplo en el editor. Míralo cuidadosamente.
class ExampleClass:
    def __init__(self,val):
        if val%2!=0:
            self.a=1
        else:
            self.b=2

example_object=ExampleClass(5)

print(example_object.a)
print(example_object.b)

# 1
# Traceback (most recent call last):
#   File "c:\Users\wccor\Python\FP2\FP2-M3_Programación Orientada a Objetos\3.3.1 POO Propiedades\Comprobando la existencia de un atributo.py", line 15, in <module>
#     print(example_object.b)
# AttributeError: 'ExampleClass' object has no attribute 'b'

"""El objeto creado por el constructor solo puede tener uno de los dos atributos posibles: a o b."""

# Como puedes ver, acceder a un atributo de objeto (clase) no existente genera una excepción AttributeError.