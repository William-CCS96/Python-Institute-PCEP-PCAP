"""Tu primer paquete: paso 8"""
# Ahora vamos hasta el final del árbol: así es como se obtiene acceso a los módulos sigma y tau.

from sys import path

path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())

# Puedes hacer tu vida más fácil usando un alias:

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())

"""Tu primer paquete: paso 9"""
# Supongamos que hemos comprimido todo el subdirectorio, comenzando desde la carpeta extra (incluyéndola), y se obtuvo un archivo llamado extrapack.zip. Después, colocamos el archivo dentro de la carpeta packages.

# Ahora podemos usar el archivo zip en un rol de paquetes:

from sys import path

path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())

# Si deseas realizar tus propios experimentos con el paquete que hemos creado, puedes descargarlo a continuación. Te alentamos a que lo hagas.

# Ahora puedes crear módulos y combinarlos en paquetes. Es hora de comenzar una discusión completamente diferente: sobre errores y fallas.