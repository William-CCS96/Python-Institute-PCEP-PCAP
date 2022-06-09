# Importando un módulo: continuación
# Ahora te mostraremos cómo pueden dos namespaces (el tuyo y el del módulo) pueden coexistir.

# Echa un vistazo al ejemplo en la ventana del editor.

# Hemos definido el nuestro propio pi y sin aquí.

# Ejecuta el programa. El código debe producir la siguiente salida:

# 0.99999999
# 1.0
# salida

# Como puedes ver, las entidades no se afectan entre sí.

import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

