"""Excepciones: continuación"""
# Observa el código en el editor. ¿Qué pasará aquí?
try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema Aritmético!")

print("FIN.")

# La primera coincidencia es la que contiene ZeroDivisionError. Significa que la consola mostrará:
    # ¡División entre Cero!
    # FIN.

# ¿Cambiará algo si intercambiamos los dos bloques except? Justo como aquí abajo:

try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema Aritmético!")
except ZeroDivisionError:
    print("¡División entre Cero!")

print("FIN.")

# El cambio es radical: la salida del código es ahora:
    # ¡Problema Aritmético!
    # FIN.

# ¿Por qué, si la excepción generada es la misma que antes?

# La excepción es la misma, pero la excepción más general ahora aparece primero: también capturará todas las divisiones entre cero. También significa que no hay posibilidad de que alguna excepción llegue a ZeroDivisionError. Ahora es completamente inalcanzable.

"""Recuerda:"""

    # ¡El orden de las excepciones importa!
    # No pongas excepciones más generales antes que otras más concretas.
    # Esto hará que el último sea inalcanzable e inútil.
    # Además, hará que el código sea desordenado e inconsistente.
    # Python no generará ningún mensaje de error con respecto a este problema.


