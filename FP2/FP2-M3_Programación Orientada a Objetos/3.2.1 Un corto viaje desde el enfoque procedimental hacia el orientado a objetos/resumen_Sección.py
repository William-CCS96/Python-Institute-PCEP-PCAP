
"""Puntos Clave"""

    # 1. Una pila es un objeto diseñado para almacenar datos utilizando el modelo LIFO. La pila normalmente realiza al menos dos operaciones, llamadas push() y pop().

    # 2. La implementación de la pila en un modelo procedimental plantea varios problemas que pueden resolverse con las técnicas ofrecidas por la POO (Programación Orientada a Objetos).

    # 3. Un método de clase es en realidad una función declarada dentro de la clase y capaz de acceder a todos los componentes de la clase.

    # 4. La parte de la clase en Python responsable de crear nuevos objetos se llama constructor y se implementa como un método de nombre __init__.

    # 5. Cada declaración de método de clase debe contener al menos un parámetro (siempre el primero) generalmente denominado self, y es utilizado por los objetos para identificarse a sí mismos.

    # 6. Si queremos ocultar alguno de los componentes de una clase del mundo exterior, debemos comenzar su nombre con __. Estos componentes se denominan privados.

"""Ejercicio 1"""
# Suponiendo que hay una clase llamada Snakes, escribe la primera línea de la declaración de clase Python, expresando el hecho de que la nueva clase es en realidad una subclase de Snake.
    # class Python(Snakes):

"""Ejercicio 2"""
# Algo falta en la siguiente declaración, ¿qué es?
# class Snakes
#     def __init__():
#         self.sound = 'Sssssss'
        # El constructor __init__() carece del parámetro obligatorio (deberíamos llamarlo self para cumplir con los estándares).

"""Ejercicio 3"""
# Modifica el código para garantizar que la propiedad venomous sea privada.
# class Snakes
#     def __init__(self):
#         self.venomous = True

# El código debería verse como sigue:
    # class Snakes
    #     def __init__(self):
    #         self.__venomous = True
