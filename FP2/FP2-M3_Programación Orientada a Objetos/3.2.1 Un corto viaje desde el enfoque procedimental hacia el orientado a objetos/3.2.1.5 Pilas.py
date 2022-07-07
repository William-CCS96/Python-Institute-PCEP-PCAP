"""La pila, el enfoque orientado a objetos: continuación"""
# Cualquier cambio que realices dentro del constructor que modifique el estado del parámetro self se verá reflejado en el objeto recien creado.

# Esto significa que puedes agregar cualquier propiedad al objeto y la propiedad permanecerá allí hasta que el objeto termine su vida o la propiedad se elimine explícitamente.

# Ahora agreguemos solo una propiedad al nuevo objeto, una lista para la pila. La nombraremos stack_list.

# Justo como aqui:

class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))


# Nota:
        # Hemos usado la notación punteada, al igual que cuando se invocan métodos. Esta es la manera general para acceder a las propiedades de un objeto: debes nombrar el objeto, poner un punto (.) después de el, y especificar el nombre de la propiedad deseada, ¡no uses paréntesis! No deseas invocar un método, deseas acceder a una propiedad.
        # Si estableces el valor de una propiedad por primera vez (como en el constructor), lo estás creando; a partir de ese momento, el objeto tiene la propiedad y está listo para usar su valor.
        # Hemos hecho algo más en el código: hemos intentado acceder a la propiedad stack_list desde fuera de la clase inmediatamente después de que se haya creado el objeto; queremos verificar la longitud actual de la pila, ¿lo hemos logrado?

# Si, por supuesto: el código produce el siguiente resultado:
# 0

# Esto no es lo que queremos de la pila. Nosotros queremos que stack_list este escondida del mundo exterior. ¿Es eso posible?
# Si, y es simple, pero no muy intuitivo.

