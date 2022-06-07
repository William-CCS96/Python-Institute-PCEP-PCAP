"""Importando un módulo"""
# Para que un módulo sea utilizable, hay que importarlo (piensa en ello como sacar un libro del estante). La importación de un módulo se realiza mediante una instrucción llamada import. Nota: import es también una palabra clave reservada (con todas sus implicaciones).

# La palabra clave reservada import

# Supongamos que deseas utilizar dos entidades proporcionadas por el módulo math:

        # Un símbolo (constante) que representa un valor preciso (tan preciso como sea posible usando aritmética de punto flotante doble) de π (aunque usar una letra griega para nombrar una variable es totalmente posible en Python, el símbolo se llama pi: es una solución más conveniente, especialmente para esa parte del mundo que ni tiene ni va a usar un Teclado Griego).
        # Una función llamada sin() (el equivalente informático de la función matemática seno).
# Ambas entidades están disponibles a través del módulo math, pero la forma en que se pueden usar depende en gran medida de como se haya realizado la importación.

# La forma más sencilla de importar un módulo en particular es usar la instrucción para importar de la siguiente manera:

import math

# La cláusula contiene:

        # La palabra reservada import.
        # El nombre del módulo que se va a importar.
# La instrucción puede colocarse en cualquier parte del código, pero debe colocarse antes del primer uso de cualquiera de las entidades del módulo.


# Si se desea (o se tiene que) importar más de un módulo, se puede hacer repitiendo la cláusula import, o listando los módulos despues de la palabra reservada import, por ejemplo:
import math
import sys

# o enumerando los módulos después de la palabra clave reservada import, como aquí:
import math, sys

# La instrucción importa dos módulos, primero uno llamado math y luego un segundo llamado sys.
# La lista de módulos puede ser arbitrariamente larga.