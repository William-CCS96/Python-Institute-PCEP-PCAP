"""
# Funciones seleccionadas del módulo platform"""
# La función platform

# El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

# Existe también una función que puede mostrar todas las capas subyacentes en un solo vistazo, llamada platform. Simplemente devuelve una cadena que describe el entorno; por lo tanto, su salida está más dirigida a los humanos que al procesamiento automatizado (lo verás pronto).

# Así es como se puede invocar:
# platform(aliased = False, terse = False)


# Y ahora:

        # aliased → cuando se establece a True (o cualquier valor distinto a cero) puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.
        # terse → cuando se establece a True (o cualquier valor distinto a cero) puede convencer a la función de presentar una forma más breve del resultado (si lo fuera posible).
# Ejecutamos el programa usando tres plataformas diferentes, esto es lo que se obtuvo:

# Intel x86 + Windows ® Vista (32 bit):

        # Windows-Vista-6.0.6002-SP2
        # Windows-Vista-6.0.6002-SP2
        # Windows-Vista
        # salida

# Intel x86 + Gentoo Linux (64 bit):

        # Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
        # Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
        # Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-glibc2.3.4
        # salida

# Raspberry PI2 + Raspbian Linux (32 bit):

        # Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
        # Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
        # Linux-4.4.0-1-rpi2-armv7l-with-glibc2.9
        # salida

# También puedes ejecutar el programa en el IDLE de tu máquina local para verificar que salida tendrá.

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))
        # Windows-10-10.0.19044-SP0
        # Windows-10-10.0.19044-SP0
        # Windows-10