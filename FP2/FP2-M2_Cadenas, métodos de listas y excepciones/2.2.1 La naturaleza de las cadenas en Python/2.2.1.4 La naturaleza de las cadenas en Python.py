char_1="a"
char_2=" "
print(ord(char_1))
print(ord(char_2))
    # 97
    # 32

char_3="²"
char_4="³"
print(ord(char_3))
print(ord(char_4))
    # 178
    # 179

char_5="α"
print(ord(char_5))
    # 945
"""
Operaciones con cadenas: ord()"""
# Si deseas saber el valor del punto de código ASCII/UNICODE de un carácter específico, puedes usar la función ord() (proveniente de ordinal).

# La función necesita una cadena de un carácter como argumento - incumplir este requisito provoca una excepción TypeError, y devuelve un número que representa el punto de código del argumento.

# Observa el código en el editor y ejecútalo. Las salida del fragmento de código es:

# 97
# 32
# salida

# Ahora asigna diferentes valores a ch1 y ch2, por ejemplo, α (letra griega alfa), y ę (una letra en el alfabeto polaco); luego ejecuta el código y ve qué resultado produce. Realiza tus propios experimentos.

