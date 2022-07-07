"""Tiempo Estimado"""
# 20-45 minutos

"""Nivel de Dificultad"""
# Fácil/Medio

"""Objetivos"""
# Mejorar las habilidades del estudiante para definir clases desde cero.
# Implementar estructuras de datos estándar como clases.

"Escenario"
# Como ya sabes, una pila es una estructura de datos que realiza el modelo LIFO (último en entrar, primero en salir). Es fácil y ya te has acostumbrado a ello perfectamente.
# Probemos algo nuevo ahora. Una cola (queue) es un modelo de datos caracterizado por el término FIFO: primero en entrar, primero en salir. Nota: una cola (fila) regular que conozcas de las tiendas u oficinas de correos funciona exactamente de la misma manera: un cliente que llegó primero también es el primero en ser atendido.

# Tu tarea es implementar la clase Queue con dos operaciones básicas:
    # put(elemento), que coloca un elemento al final de la cola.
# get(), que toma un elemento del principio de la cola y lo devuelve como resultado (la cola no puede estar vacía para realizarlo correctamente).
"""Sigue las sugerencias:"""

    # Emplea una lista como tu almacenamiento (como lo hicimos con la pila).
    # put() debe agregar elementos al principio de la lista, mientras que get() debe eliminar los elementos del final de la lista.
    # Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) y generala cuando get() intentes operar en una lista vacía.
# Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si tu salida es similar a la nuestra.



# Salida Esperada
# 1
# perro
# False
# Error de Cola

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__list=[]

    def put(self, elem):
        """Inserta elem en el final de la cola"""
        self.__list.append(elem)

    def get(self):
        """Elimina el primer elimento de la pila y lo retorna, si la pila esta vacia genera una excepción"""
        if len(self.__list)>0:
            return self.__list.pop(0)
        else:
            raise QueueError

    def vacia(self):
        """Devuelve True si la pila esta vacía ó False si no."""
        return self.__list==[]


que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")

print(que.get())