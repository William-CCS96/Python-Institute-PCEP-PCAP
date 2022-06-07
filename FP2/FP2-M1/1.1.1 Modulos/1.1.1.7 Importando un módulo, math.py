
# Importando un módulo: continuación
# En el segundo método, la sintaxis del import señala con precisión que entidad (o entidades) del módulo son aceptables en el código:

from math import pi


# La instrucción consta de los siguientes elementos:

    # La palabra clave reservada from.
    # El nombre del módulo a ser (selectivamente) importado.
    # La palabra clave reservada import.
    # El nombre o lista de nombres de la entidad o entidades las cuales estan siendo importadas al namespace.
    # La instrucción tiene este efecto:

    # Las entidades listadas son las únicas que son importadas del módulo indicado.
    # Los nombres de las entidades importadas pueden ser accedidas dentro del código sin especificar el nombre del módulo de origen.
# Nota: no se importan otras entidades, únicamente las especificadas. Además, no se pueden importar entidades adicionales utilizando una línea como esta:

"""print(math.e)"""
# Esto ocasionará un error, (e es la constante de Euler: 2.71828...).

# Reescribamos el código anterior para incorporar esta nueva técnica.
# Aquí está:
from math import sin, pi

print(sin(pi/2))


# El resultado debe de ser el mismo que el anterior, se han empleado las mismas entidades: 1.0. Copia y pega el código en el editor, y ejecuta el programa.

# ¿El código parece más simple? Quizás, pero el aspecto no es el único efecto de este tipo de importación. Veamos más a detalle esto.

