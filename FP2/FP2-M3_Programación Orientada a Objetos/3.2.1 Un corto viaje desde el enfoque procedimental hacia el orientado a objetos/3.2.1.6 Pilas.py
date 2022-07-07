"""La pila, el enfoque orientado a objetos: continuación"""
# Echa un vistazo: hemos agregado dos guiones bajos antes del nombre stack_list, nada mas:

class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()
print(len(stack_object.__stack_list))

# El cambio invalida el programa.
# ¿Por qué?

"""Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), se vuelve privado, esto significa que solo se puede acceder desde dentro de la clase.

No puedes verlo desde el mundo exterior. Así es como Python implementa el concepto de encapsulación."""

# Ejecuta el programa para probar nuestras suposiciones: una excepción AttributeError debe ser generada.



