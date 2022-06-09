"""Operaciones con cadenas: min()"""
# Ahora que comprendes que las cadenas son secuencias, podemos mostrarte algunas capacidades de secuencia menos obvias. Las presentaremos utilizando cadenas, pero no olvides que las listas también pueden adoptar los mismos trucos.

# Comenzaremos con la función llamada min().

# Esta función encuentra el elemento mínimo de la secuencia pasada como argumento. Existe una condición - la secuencia (cadena o lista) no puede estar vacía, de lo contrario obtendrás una excepción ValueError.

# El programa Ejemplo 1 da la siguiente salida:
# Nota: Es una A mayúscula. ¿Por qué? Recuerda la tabla ASCII, ¿qué letras ocupan las primeras posiciones, mayúsculas o minúsculas?

# Hemos preparado dos ejemplos más para analizar: Ejemplos 2 y 3.
# Como puedes ver, presentan más que solo cadenas. El resultado esperado se ve de la siguiente manera:
# Nota: hemos utilizado corchetes para evitar que el espacio se pase por alto en tu pantalla.


# Demonstrando min() - Ejemplo 1:
print(min("aAbByYzZ"))
    # A

# Demonstrando min() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')
    # [ ]

t = [0, 1, 2]
print(min(t))
    # 0
