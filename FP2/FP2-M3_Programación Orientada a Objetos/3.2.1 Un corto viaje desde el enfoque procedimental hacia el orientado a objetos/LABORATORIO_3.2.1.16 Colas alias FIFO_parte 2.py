"""Tiempo Estimado"""
# 15-30 minutos
"""Nivel de Dificultad"""
# Fácil/Medio

"""Objetivos"""
# Mejorar las habilidades del estudiante para definir subclases.
# Agregar nueva funcionalidad a una clase existente.
"""Escenario"""
# Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método sin parámetros que devuelva True si la cola está vacía y False de lo contrario.

# Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un resultado similar al nuestro.

# A continuación, puedes copiar el código que usamos en el laboratorio anterior:





class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue=[]

    def put(self, elem):
        """Inserta elem en el final de la cola"""
        self.queue.append(elem)

    def get(self):
        """Elimina el primer elimento de la pila y lo retorna, si la pila esta vacia genera una excepción"""
        if len(self.queue)>0:
            return self.queue.pop(0)
        else:
            raise QueueError

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    def isempty(self):
        """Devuelve True si la pila esta vacía ó False si no."""
        if self.queue==[]:
            return True
        else:
            return False



que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)


for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")



