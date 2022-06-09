"""Funciones seleccionadas del módulo platform: continuación"""
# La función system

# Una función llamada system() devuelve el nombre genérico del sistema operativo en una cadena.

# Nuestras plataformas de ejemplo se presentan de la siguiente manera:

# Intel x86 + Windows ® Vista (32 bit):
        # Windows

# Intel x86 + Gentoo Linux (64 bit):
        # Linux

# Raspberry PI2 + Raspbian Linux (32 bit):
        # Linux

from platform import system

print(system())
        # Windows