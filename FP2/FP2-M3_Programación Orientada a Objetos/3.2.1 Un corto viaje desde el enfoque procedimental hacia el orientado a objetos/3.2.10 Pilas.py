"""El enfoque orientado a objetos: una pila desde cero (continuación)"""
# Ahora vamos un poco mas lejos. Vamos a agregar una nueva clase para manejar pilas.

# La nueva clase debería poder evaluar la suma de todos los elementos almacenados actualmente en la pila.

# No queremos modificar la pila previamente definida. Ya es lo suficientemente buena en sus aplicaciones, y no queremos que cambie de ninguna manera. Queremos una nueva pila con nuevas capacidades. En otras palabras, queremos construir una subclase de la ya existente clase Stack.

# El primer paso es fácil: solo define una nueva subclase que apunte a la clase que se usará como superclase.

# Así es como se ve:

"""class AddingStack(Stack):
    pass"""


# La clase aún no define ningún componente nuevo, pero eso no significa que esté vacía. Obtiene (hereda) todos los componentes definidos por su superclase, el nombre de la superclase se escribe después de los dos puntos, después del nombre de la nueva clase.

# Esto es lo que queremos de la nueva pila:

        # Queremos que el método push no solo inserte el valor en la pila, sino que también sume el valor a la variable sum.
        # Queremos que la función pop no solo extraiga el valor de la pila, sino que también reste el valor de la variable sum.

# En primer lugar, agreguemos una nueva variable a la clase. Será una variable privada, al igual que la lista de pila. No queremos que nadie manipule el valor de la variable sum.

# Como ya sabes, el constructor agrega una nueva propiedad a la clase. Ya sabes como hacerlo, pero hay algo realmente intrigante dentro del constructor. Echa un vistazo:

"""class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
"""

# La segunda línea del cuerpo del constructor crea una propiedad llamada __sum, almacenará el total de todos los valores de la pila.
# Pero la línea anterior se ve diferente. ¿Qué hace? ¿Es realmente necesaria? Sí lo es.

"""Al contrario de muchos otros lenguajes, Python te obliga a invocar explícitamente el constructor de una superclase. Omitir este punto tendrá efectos nocivos: el objeto se verá privado de la lista __stack_list. Tal pila no funcionará correctamente.

Esta es la única vez que puedes invocar a cualquiera de los constructores disponibles explícitamente; se puede hacer dentro del constructor de la superclase."""

# Ten en cuenta la sintaxis:

        # Se especifica el nombre de la superclase (esta es la clase cuyo constructor se desea ejecutar).
        # Se pone un punto (.) después del nombre.
        # Se especifica el nombre del constructor.
        # Se debe señalar al objeto (la instancia de la clase) que debe ser inicializado por el constructor; es por eso que se debe especificar el argumento y utilizar la variable self aquí; recuerda: invocar cualquier método (incluidos los constructores) desde fuera de la clase nunca requiere colocar el argumento self en la lista de argumentos, invocar un método desde dentro de la clase exige el uso explícito del argumento self, y tiene que ser el primero en la lista.
# Nota: generalmente es una práctica recomendada invocar al constructor de la superclase antes de cualquier otra inicialización que desees realizar dentro de la subclase. Esta es la regla que hemos seguido en el código.


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class addingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0

