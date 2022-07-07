"""La pila, el enfoque orientado a objetos"""
# Por supuesto, la idea principal sigue siendo la misma. Usaremos una lista como almacenamiento de la pila. Solo tenemos que saber como poner la lista en la clase.

# Comencemos desde el principio: así es como comienza la pila orientada a objetos:
"""class Stack:"""

# Ahora, esperamos dos cosas de la clase:

#         Queremos que la clase tenga una propiedad como el almacenamiento de la pila, tenemos que "instalar" una lista dentro de cada objeto de la clase (nota: cada objeto debe tener su propia lista; la lista no debe compartirse entre diferentes pilas).
#         Despues, queremos que la lista esté oculta de la vista de los usuarios de la clase.
# ¿Cómo se hace esto?

# A diferencia de otros lenguajes de programación, Python no tiene medios para permitirte declarar una propiedad como esa.

# En su lugar, debes agregar una instrucción específica. Las propiedades deben agregarse a la clase manualmente.

# ¿Cómo garantizar que dicha actividad tiene lugar cada vez que se crea una nueva pila?

# Existe una manera simple de hacerlo, tienes que equipar a la clase con una función específica:

        # Tiene que ser nombrada de forma estricta.
        # Se invoca implícitamente cuando se crea el nuevo objeto.
# Dicha función es llamada el constructor, ya que su propósito general es construir un nuevo objeto. El constructor debe saber todo acerca de la estructura del objeto y debe realizar todas las inicializaciones necesarias.

# Agreguemos un constructor muy simple a la nueva clase. Echa un vistazo al código:

class Stack:
    def __init__(self):
        print("¡Hola!")


stack_object = Stack()

# Expliquemos más a detalle:
    # El nombre del constructor es siempre __init__.
    # Tiene que tener al menos un parámetro (discutiremos esto más adelante); el parámetro se usa para representar el objeto recién creado: puedes usar el parámetro para manipular el objeto y enriquecerlo con las propiedades necesarias; harás uso de esto pronto.
    # Nota: el parámetro obligatorio generalmente se denomina self, es solo una sugerencía, pero deberías seguirla, simplifica el proceso de lectura y comprensión de tu código.

# Aquí está su salida:
# ¡Hola!

# Nota: no hay rastro de la invocación del constructor dentro del código. Ha sido invocado implícita y automáticamente. Hagamos uso de eso ahora.