"""Funciones seleccionadas del módulo random"""
# La función random

# La función general llamada random() (no debe confundirse con el nombre del módulo) produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).

# El programa de ejemplo a continuación producirá cinco valores pseudoaleatorios, ya que sus valores están determinados por el valor semilla actual (bastante impredecible), no puedes adivinarlos:

from random import random

for i in range(5):
    print(random())


# Ejecuta el programa. Esto es lo que tenemos:

        # 0.9535768927411208
        # 0.5312710096244534
        # 0.8737691983477731
        # 0.5896799172452125
        # 0.02116716297022092


"""La función seed"""

# La función seed() es capaz de directamente establecer la semilla del generador. Te mostramos dos de sus variantes:

# seed() - establece la semilla con la hora actual.
# seed(int_value) - establece la semilla con el valor entero int_value.
# Hemos modificado el programa anterior; de hecho, hemos eliminado cualquier rastro de aleatoriedad del código:

from random import random, seed

seed(0)

for i in range(5):
    print(random())


# Debido al hecho de que la semilla siempre se establece con el mismo valor, la secuencia de valores generados siempre se ve igual.
# Ejecuta el programa. Esto es lo que tenemos:

        # 0.844421851525
        # 0.75795440294
        # 0.420571580831
        # 0.258916750293
        # 0.511274721369


# ¿Y tú?

# Nota: tus valores pueden ser ligeramente diferentes si tu sistema utiliza aritmética de punto flotante más precisa o menos precisa, pero la diferencia se verá bastante lejos del punto decimal.