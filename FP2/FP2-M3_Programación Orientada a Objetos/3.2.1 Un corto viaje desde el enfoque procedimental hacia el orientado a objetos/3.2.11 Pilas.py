"""El enfoque orientado a objetos: una pila desde cero (continuación)"""
# En segundo lugar, agreguemos dos métodos. Pero, ¿realmente estamos agregándolos? Ya tenemos estos métodos en la superclase. ¿Podemos hacer algo así?

# Si podemos. Significa que vamos a cambiar la funcionalidad de los métodos, no sus nombres. Podemos decir con mayor precisión que la interfaz (la forma en que se manejan los objetos) de la clase permanece igual al cambiar la implementación al mismo tiempo.

# Comencemos con la implementación de la función push. Esto es lo que esperamos de la función:

    # Agregar el valor a la variable __sum.
    # Agregar el valor a la pila.
# Nota: la segunda actividad ya se implementó dentro de la superclase, por lo que podemos usarla. Además, tenemos que usarla, ya que no hay otra forma de acceder a la variable __stackList.

# Así es como se mira el método push dentro de la subclase:

def push(self, val):
    self.__sum += val
    Stack.push(self, val)


# Toma en cuenta la forma en que hemos invocado la implementación anterior del método push (el disponible en la superclase):

        # Tenemos que especificar el nombre de la superclase; esto es necesario para indicar claramente la clase que contiene el método, para evitar confundirlo con cualquier otra función del mismo nombre.
        # Tenemos que especificar el objeto de destino y pasarlo como primer argumento (no se agrega implícitamente a la invocación en este contexto).
# Se dice que el método push ha sido anulado, el mismo nombre que en la superclase ahora representa una funcionalidad diferente.


class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
    

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0

    def push(self,val):
        self.__sum+=val
        Stack.push(self,val)

    def pop(self):
        val=Stack.pop(self)
        self.__sum-=val
        return val


    
