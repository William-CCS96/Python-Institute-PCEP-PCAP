"""Funciones seleccionadas del módulo math"""
# Comencemos con una vista previa de algunas de las funciones proporcionadas por el módulo math.

# Se han elegido algunas arbitrariamente, pero esto no significa que las funciones no mencionadas aquí sean menos significativas. Tómate el tiempo para revisar las demás por ti mismo: no tenemos el espacio ni el tiempo para hablar de todas a detalle.

# El primer grupo de funciones de módulo math están relacionadas con trigonometría:

        # sin(x) → el seno de x.
        # cos(x) → el coseno de x.
        # tan(x) → la tangente de x.
# Todas estas funciones toman un argumento (una medida de ángulo expresada en radianes) y devuelven el resultado apropiado (ten cuidado con tan() - no todos los argumentos son aceptados).

# Por supuesto, también están sus versiones inversas:

        # asin(x) → el arcoseno de x.
        # acos(x) → el arcocoseno de x.
        # atan(x) → el arcotangente de x.
# Estas funciones toman un argumento (verifican que sea correcto) y devuelven una medida de un ángulo en radianes.


# Para trabajar eficazmente con mediciones de ángulos, el módulo math proporciona las siguientes entidades:

        # pi → una constante con un valor que es una aproximación de π.
        # radians(x) → una función que convierte x de grados a radianes.
        # degrees(x) → una función que convierte x de radianes a grados.
# Ahora observa el código en el editor. El programa de ejemplo no es muy sofisticado, pero ¿puedes predecir sus resultados?


# Además de las funciones circulares (enumeradas anteriormente), el módulo math también contiene un conjunto de sus análogos hiperbólicos:

        # sinh(x) → el seno hiperbólico.
        # cosh(x) → el coseno hiperbólico.
        # tanh(x) → la tangente hiperbólico.
        # asinh(x) → el arcoseno hiperbólico.
        # acosh(x) → el arcocoseno hiperbólico.
        # atanh(x) → el arcotangente hiperbólico.


from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
