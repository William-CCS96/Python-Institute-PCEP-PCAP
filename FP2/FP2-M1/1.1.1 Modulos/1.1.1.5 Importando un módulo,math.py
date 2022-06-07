"""Importando un módulo: continuación"""
# Observa el fragmento a continuación, esta es la forma en que se habilitan los nombres de pi y sin con el nombre de su módulo de origen:

# math.pi
# math.sin


# Es sencillo, se pone:
        # El nombre del módulo (math).
        # Un punto.
        # El nombre de la entidad (pi).

# Tal forma indica claramente el namespace en el que existe el nombre.

# Nota: el uso de esto es obligatorio si un módulo ha sido importado con la instrucción import. No importa si alguno de los nombres del código y del namespace del módulo están en conflicto o no.


# Este primer ejemplo no será muy avanzado: solo se desea imprimir el valor de sin((½π).
# Observa el código en el editor. Así es como se prueba.
# El código genera el valor esperado: 1.0.

# Nota: el eliminar cualquiera de las dos indicaciones del nombre del módulo hará que el código sea erróneo. No hay otra forma de entrar al namespace de math si se hizo lo siguiente:

# import math

import math
print(math.sin(math.pi/2))
