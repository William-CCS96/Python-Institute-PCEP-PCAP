
"""Importando un módulo: *"""
# En el tercer método, la sintaxis del import es una forma más agresiva que la presentada anteriormente:

from module import *


# Como puedes ver, el nombre de una entidad (o la lista de nombres de entidades) se reemplaza con un solo asterisco (*).

# Tal instrucción importa todas las entidades del módulo indicado.

# ¿Es conveniente? Sí, lo es, ya que libera del deber de enumerar todos los nombres que se necesiten.

# ¿Es inseguro? Sí, a menos que conozcas todos los nombres proporcionados por el módulo, es posible que no puedas evitar conflictos de nombres. Trata esto como una solución temporal e intenta no usarlo en un código regular.

"""
Importando un módulo: la palabra clave reservada as"""
# Si se importa un módulo y no se esta conforme con el nombre del módulo en particular (por ejemplo, si es el mismo que el de una de sus entidades ya definidas) puede dársele otro nombre: esto se llama aliasing o renombrado.

# Aliasing (renombrado) hace que el módulo se identifique con un nombre diferente al original. Esto también puede acortar los nombres originales.

# La creación de un alias se realiza junto con la importación del módulo, y exige la siguiente forma de la instrucción import:

import module as alias

# El "module" identifica el nombre del módulo original mientras que el "alias" es el nombre que se desea usar en lugar del original.
# Nota: as es una palabra clave reservada.
