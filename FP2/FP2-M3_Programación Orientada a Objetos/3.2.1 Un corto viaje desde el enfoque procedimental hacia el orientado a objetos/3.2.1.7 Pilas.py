"""El enfoque orientado a objetos: una pila desde cero"""
# Ahora es el momento de que las dos funciones (métodos) implementen las operaciones push y pop. Python supone que una función de este tipo debería estar inmersa dentro del cuerpo de la clase, como el constructor.

# Queremos invocar estas funciones para agregar(push) y quitar(pop) valores de la pila. Esto significa que ambos deben ser accesibles para el usuario de la clase (en contraste con la lista previamente construida, que está oculta para los usuarios de la clase ordinaria).

# Tal componente es llamado público, por ello no puede comenzar su nombre con dos (o más) guiones bajos. Hay un requisito más el nombre no debe tener más de un guión bajo.

# Las funciones en sí son simples. Echa un vistazo:

class Stack():
    def __init__(self):
        self.__stack_list=[]
    
    def push(self,val):
        self.__stack_list.append(val)

    def pop(self):
        val=self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object=Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(type(stack_object))

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

# Sin embargo, hay algo realmente extraño en el código. Las funciones parecen familiares, pero tienen más parámetros que sus contrapartes procedimentales.

# Aquí, ambas funciones tienen un parámetro llamado self en la primera posición de la lista de parámetros.

# ¿Es necesario? Si, lo es.

# Todos los métodos deben tener este parámetro. Desempeña el mismo papel que el primer parámetro constructor.

# Permite que el método acceda a entidades (propiedades y actividades / métodos) del objeto. No puedes omitirlo. Cada vez que Python invoca un método, envía implícitamente el objeto actual como el primer argumento.

# Esto significa que el método está obligado a tener al menos un parámetro, que Python mismo utiliza, no tienes ninguna influencia sobre el.

# Si tu método no necesita ningún parámetro, este debe especificarse de todos modos. Si está diseñado para procesar solo un parámetro, debes especificar dos, ya que la función del primero sigue siendo la misma.

# Hay una cosa más que requiere explicación: la forma en que se invocan los métodos desde la variable __stack_list.

# Afortunadamente, es mucho más simple de lo que parece:

# La primera etapa entrega el objeto como un todo → self.
# A continuación, debes llegar a la lista __stack_list → self.__stack_list.
# Con __stack_list lista para ser usada, puedes realizar el tercer y último paso → self.__stack_list.append(val).
# La declaración de la clase está completa y se han enumerado todos sus componentes. La clase está lista para usarse.

