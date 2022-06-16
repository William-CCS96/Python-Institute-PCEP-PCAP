"""Comparando cadenas"""
# Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.
# Observa estos operadores: también sirven para comparar cadenas:
    # ==
    # !=
    # >
    # >=
    # <
    # <=
# Existe un "pero": los resultados de tales comparaciones a veces pueden ser un poco sorprendentes. No olvides que Python no es consciente (no puede serlo de ninguna manera) de problemas lingüísticos sutiles, simplemente compara valores de puntos de código, carácter por carácter.
# Los resultados que se obtienen de una operación de este tipo a veces son sorprendentes. Comencemos con los casos más simples.

# Dos cadenas son iguales cuando consisten de los mismos caracteres en el mismo orden. Del mismo modo, dos cadenas no son iguales cuando no consisten de los mismos caracteres en el mismo orden.

# Ambas comparaciones dan True (verdadero) como resultado:

'alpha' == 'alpha'
'alpha' != 'Alpha'

# La relación entre cadenas se determina al comparar el primer carácter diferente en ambas cadenas (ten en cuenta los puntos de código ASCII / UNICODE en todo momento).
# Cuando se comparan dos cadenas de diferentes longitudes y la más corta es idéntica a la más larga, la cadena más larga se considera mayor.

'alpha' < 'alphabet'
# La comparación es True (verdadera).

# La comparación de cadenas siempre distingue entre mayúsculas y minúsculas (las letras mayúsculas se consideran menores en comparación con las minúsculas).

# La expresión es True (verdadera):
'beta' > 'Beta'
