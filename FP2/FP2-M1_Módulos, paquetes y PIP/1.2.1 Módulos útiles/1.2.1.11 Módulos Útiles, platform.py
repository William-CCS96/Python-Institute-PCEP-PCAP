"""Funciones seleccionadas del módulo platform: continuación"""
# La función machine

# En ocasiones, es posible que solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo junto con Python y el código, una función llamada machine() te lo dirá. Como anteriormente, la función devuelve una cadena.

# Nuevamente, ejecutamos el programa en tres plataformas diferentes:

# Intel x86 + Windows ® Vista (32 bit):
        # x86

# Intel x86 + Gentoo Linux (64 bit):
        # x86_64

# Raspberry PI2 + Raspbian Linux (32 bit):
        # armv7l
from platform import machine

print(machine())
        # AMD64
        