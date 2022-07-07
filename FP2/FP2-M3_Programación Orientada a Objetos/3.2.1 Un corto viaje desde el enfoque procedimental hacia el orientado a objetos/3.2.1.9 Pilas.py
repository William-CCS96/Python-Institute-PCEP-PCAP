"""El enfoque orientado a objetos: una pila desde cero (continuación)"""
# Analiza el fragmento de código a continuación: hemos creado tres objetos de la clase Stack. Después, hemos hecho malabarismos. Intenta predecir el valor que se muestra en la pantalla.

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop()+1)
funny_stack.push(another_stack.pop()-2)

print(funny_stack.pop())
    # 0

    