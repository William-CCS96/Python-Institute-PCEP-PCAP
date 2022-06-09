"""Tu primer paquete: paso 7"""
# Vamos a acceder a la función funI() del módulo iota del paquete extra. Nos obliga a usar nombres de paquetes calificados (asocia esto al nombramiento de carpetas y subcarpetas).

# Así es como se hace:
from sys import path
path.append('..\\packages')

import extra.iota
print(extra.iota.funI())

# Nota:
        # Hemos modificado la variable path para que sea accesible a Python.
        # El import no apunta directamente al módulo, pero especifica la ruta completa desde la parte superior del paquete.
# El reemplazar import extra.iota con import iota causará un error.

# La siguiente variante también es válida:

from sys import path
path.append('..\\packages')

from extra.iota import funI
print(funI())

# Nota el nombre calificado del módulo iota.