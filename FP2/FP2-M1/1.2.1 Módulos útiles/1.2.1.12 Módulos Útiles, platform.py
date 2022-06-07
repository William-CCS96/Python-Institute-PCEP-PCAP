"""Funciones seleccionadas del módulo platform: continuación"""
# La función processor

# La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).
# Una vez más, ejecutamos el programa en tres plataformas diferentes:

# Intel x86 + Windows ® Vista (32 bit):
            # x86

# Intel x86 + Gentoo Linux (64 bit):
            # Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz

# Raspberry PI2 + Raspbian Linux (32 bit):
            # armv7l

# Prueba esto en tu máquina local.

from platform import processor

print(processor())
        # Intel64 Family 6 Model 142 Stepping 9, GenuineIntel