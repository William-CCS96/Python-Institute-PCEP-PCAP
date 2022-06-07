
# Funciones seleccionadas del módulo platform: continuación

# La función version
# La versión del sistema operativo se proporciona como una cadena por la función version().

# Ejecuta el código y verifica su salida. Esto es lo que tenemos:

# Intel x86 + Windows ® Vista (32 bit):
        # 6.0.6002

# Intel x86 + Gentoo Linux (64 bit):
        #1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017

# Raspberry PI2 + Raspbian Linux (32 bit):
        #1 SMP Debian 4.4.6-1+rpi14 (2016-05-05)

from platform import version

print(version())
        # 10.0.19044