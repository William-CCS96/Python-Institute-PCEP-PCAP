"""Comparando cadenas: continuación"""
# Aún si una cadena contiene solo dígitos, todavía no es un número. Se interpreta como lo que es, como cualquier otra cadena regular, y su aspecto numérico (potencial) no se toma en cuenta, en ninguna manera.

# Observa los ejemplos:
'10' == '010'
'10' > '010'
'10' > '8'
'20' < '8'
'20' < '80'
    # False
    # True
    # False
    # True
    # True

"""El comparar cadenas con los números generalmente es una mala idea."""
# Las únicas comparaciones que puede realizar con impunidad son aquellas simbolizadas por los operadores == y !=. El primero siempre devuelve False (falso), mientras que el segundo siempre devuelve True (verdadero).

# El uso de cualquiera de los operadores de comparación restantes generará una excepción TypeError.
# Vamos a verlo:

'10' == 10
'10' != 10
'10' == 1
'10' != 1
'10' > 10
    # False
    # True
    # False
    # True
    # TypeError exception


print("5">"4")