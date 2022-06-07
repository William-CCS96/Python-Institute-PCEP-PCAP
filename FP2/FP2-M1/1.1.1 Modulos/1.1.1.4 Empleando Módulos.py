"""Importando un módulo: continuación"""
# Para continuar, debes familiarizarte con un término importante: namespace. No te preocupes, no entraremos en detalles: esta explicación será lo más breve posible.

# Un namespace es un espacio (entendido en un contexto no físico) en el que existen algunos nombres y los nombres no entran en conflicto entre sí (es decir, no hay dos objetos diferentes con el mismo nombre). Podemos decir que cada grupo social es un namespace - el grupo tiende a nombrar a cada uno de sus miembros de una manera única (por ejemplo, los padres no darían a sus hijos el mismo nombre).

# El concepto de namespace
# Esta singularidad se puede lograr de muchas maneras, por ejemplo, mediante el uso de apodos junto con los nombres (funcionará dentro de un grupo pequeño como una clase en una escuela) o asignando identificadores especiales a todos los miembros del grupo (el número de Seguro Social de EE. UU. es un buen ejemplo de tal práctica).

# Dentro de un determinado namespace, cada nombre debe permanecer único. Esto puede significar que algunos nombres pueden desaparecer cuando cualquier otra entidad de un nombre ya conocido ingresa al namespace. Mostraremos como funciona y como controlarlo, pero primero, volvamos a las importaciones.

# Si el módulo de un nombre especificado existe y es accesible (un módulo es de hecho un archivo fuente de Python), Python importa su contenido, se hacen conocidos todos los nombres definidos en el módulo, pero no ingresan al namespace del código.

# Esto significa que puedes tener tus propias entidades llamadas sin o pi y no serán afectadas en alguna manera por la importación.

# En este punto, es posible que te estes preguntando como acceder al pi el cual viene del módulo math.
# Para hacer esto, se debe de mandar llamar el pi con el nombre del módulo original.

