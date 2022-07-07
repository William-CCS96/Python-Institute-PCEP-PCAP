"""El enfoque orientado a objetos: una pila desde cero (continuación)"""
# Esta es la nueva función pop:

        # def pop(self):
        #     val = Stack.pop(self)
        #     self.__sum -= val
        #     return val

# Hasta ahora, hemos definido la variable __sum, pero no hemos proporcionado un método para obtener su valor. Parece estar escondido. ¿Cómo podemos mostrarlo y que al mismo tiempo que se proteja de modificaciones?

# Tenemos que definir un nuevo método. Lo nombraremos get_sum. Su única tarea será devolver el valor de __sum.
# Aquí está:

        # def get_sum(self):
        #     return self.__sum

# Entonces, veamos el programa en el editor. El código completo de la clase está ahí. Podemos ahora verificar su funcionamiento, y lo hacemos con la ayuda de unas pocas líneas de código adicionales.
# Como puedes ver, agregamos cinco valores subsiguientes en la pila, imprimimos su suma y los sacamos todos de la pila.
# Bien, esta ha sido una breve introducción a la programación de orientada a objetos de Python. Pronto te contaremos todo con más detalle.

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0

    def get_sum(self):
        return self.__sum

    def push(self,val):
        self.__sum+=val
        Stack.push(self,val)

    def pop(self):
        val=Stack.pop(self)
        self.__sum-=val
        return val

stack_object=AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())