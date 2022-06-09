"""Puntos Clave
# """
# 1. Una función llamada dir() puede mostrarte una lista de las entidades contenidas dentro de un módulo importado. Por ejemplo:
    # import os
    # dir(os)
    # Imprime una lista de todo el contenido del módulo os el cual, puedes usar en tu código.

# 2. El módulo math contiene más de 50 funciones y constantes que realizan operaciones matemáticas (como sine(), pow(), factorial()) o aportando valores importantes (como π y la constante de Euler e).

# 3. El módulo random agrupa más de 60 entidades diseñadas para ayudarte a usar números pseudoaleatorios. No olvides el prefijo "pseudo", ya que no existe un número aleatorio real cuando se trata de generarlos utilizando los algoritmos de la computadora.

# 4. El módulo platform contiene alrededor de 70 funciones que te permiten sumergirte en las capas subyacentes del sistema operativo y el hardware. Usarlos te permite aprender más sobre el entorno en el que se ejecuta tu código.

# 5. El Índice de Módulos de Python (https://docs.python.org/3/py-modindex.html es un directorio de módulos impulsado por la comunidad disponible en el universo de Python. Si deseas encontrar un módulo que se adapte a tus necesidades, comienza tu búsqueda allí.

#-----------------
# Ejercicio 1

# ¿Cuál es el valor esperado de la variable result después de que se ejecuta el siguiente código?
import math
result = math.e == math.exp(1)
    # True

# Ejercicio 2
# (Completa el enunciado) Establecer la semilla del generador con el mismo valor cada vez que se ejecuta tu programa garantiza que ...
    
    # ... los valores pseudoaleatorios emitidos desde el módulo random serán exactamente los mismos.

# Ejercicio 3   
    # ¿Cuál de las funciones del módulo platform utilizarías para determinar el nombre del CPU que corre dentro de tu computadora?
        # La función processor()

# Ejercicio 4
# ¿Cuál es el resultado esperado del siguiente fragmento de código?

import platform
print(len(platform.python_version_tuple()))
    # 3