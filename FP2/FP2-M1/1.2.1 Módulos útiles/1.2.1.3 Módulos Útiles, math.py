
# Funciones seleccionadas del módulo math: continuación
# Existe otro grupo de las funciones math relacionadas con la exponenciación:

"""        # e → una constante con un valor que es una aproximación del número de Euler (e).
        # exp(x) → encontrar el valor de ex.
        # log(x) → el logaritmo natural de x.
        # log(x, b) → el logaritmo de x con base b.
        # log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
        # log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).
        # Nota: la función pow():"""

"""        # pow(x, y) → encuentra el valor de x**y (toma en cuenta los dominios)."""
# Esta es una función incorporada y no se tiene que importar.
# Observa el código en el editor. ¿Puedes predecir su salida?

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

print(pow(4,2))


