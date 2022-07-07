"""Tu primera clase"""
# La programación orientada a objetos es el arte de definir y expandir clases. Una clase es un modelo de una parte muy específica de la realidad, que refleja las propiedades y actividades que se encuentran en el mundo real.

# Las clases definidas al principio son demasiado generales e imprecisas para cubrir el mayor número posible de casos reales.

# No hay obstáculo para definir nuevas subclases más precisas. Heredarán todo de su superclase, por lo que el trabajo que se utilizó para su creación no se desperdicia.

# La nueva clase puede agregar nuevas propiedades y nuevas actividades y, por lo tanto, puede ser más útil en aplicaciones específicas. Obviamente, se puede usar como una superclase para cualquier número de subclases recién creadas.

# El proceso no necesita tener un final. Puedes crear tantas clases como necesites.

# La clase que se define no tiene nada que ver con el objeto: la existencia de una clase no significa que ninguno de los objetos compatibles se creará automáticamente. La clase en sí misma no puede crear un objeto: debes crearlo tu mismo y Python te permite hacerlo.

# Es hora de definir la clase más simple y crear un objeto. Analiza el siguiente ejemplo:
class TheSimplestClass:
    pass

#  clase. La clase es bastante pobre: no contiene propiedades ni actividades. Esta vacía, pero eso no importa por ahora. Cuanto más simple sea la clase, mejor para nuestros propósitos.

# La definición comienza con la palabra clave reservada class. La palabra clave reservada es seguida por un identificador que le dará nombre a la clase (nota: no lo confundas con el nombre del objeto: estas son dos cosas diferentes).

# A continuación, se agregan dos puntos (:), como clases, como funciones, forman su propio bloque anidado. El contenido dentro del bloque define todas las propiedades y actividades de la clase.

# La palabra clave reservada pass llena la clase con nada. No contiene ningún método ni propiedades.

"""Tu primer objeto"""
# La clase recién definida se convierte en una herramienta que puede crear nuevos objetos. La herramienta debe usarse explícitamente, bajo demanda.

# Imagina que deseas crear un objeto (exactamente uno) de la clase TheSimplestClass.

# Para hacer esto, debes asignar una variable para almacenar el objeto recién creado de esa clase y crear un objeto al mismo tiempo.

# Se hace de la siguiente manera:

my_first_object=TheSimplestClass()

# Nota:
#     El nombre de la clase intenta fingir que es una función, ¿puedes ver esto? Lo discutiremos pronto.
#     El objeto recién creado está equipado con todo lo que trae la clase. Como esta clase está completamente vacía, el objeto también está vacío.
#     El acto de crear un objeto de la clase seleccionada también se llama instanciación (ya que el objeto se convierte en una instancia de la clase).

# Dejemos las clases en paz por un breve momento, ya que ahora diremos algunas palabras sobre pilas. Sabemos que el concepto de clases y objetos puede no estar completamente claro todavía. No te preocupes, te explicaremos todo muy pronto.


