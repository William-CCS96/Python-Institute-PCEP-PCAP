# Veamos algunos métodos estándar de cadenas en Python. Vamos a analizarlos en orden alfabético, cualquier orden tiene tanto desventajas como ventajas, por lo que la elección puede ser aleatoria.

# El método capitalize() hace exactamente lo que dice - crea una nueva cadena con los caracteres tomados de la cadena fuente, pero intenta modificarlos de la siguiente manera:

# Si el primer carácter dentro de la cadena es una letra (nota: el primer carácter es el elemento con un índice igual a 0, no es el primer carácter visible), se convertirá a mayúsculas.
# Todas las letras restantes de la cadena se convertirán a minúsculas.
# No olvides que:

# La cadena original desde la cual se invoca el método no se cambia de ninguna manera, la inmutabilidad de una cadena debe obedecerse sin reservas.
# La cadena modificada (en mayúscula en este caso) se devuelve como resultado; si no se usa de alguna manera (asígnala a una variable o pásala a una función / método) desaparecerá sin dejar rastro.
# Nota: los métodos no tienen que invocarse solo dentro de las variables. Se pueden invocar directamente desde dentro de literales de cadena. Usaremos esa convención regularmente: simplificará los ejemplos, ya que los aspectos más importantes no desaparecerán entre asignaciones innecesarias.

# Echa un vistazo al ejemplo en el editor. Ejecútalo.z|

# Esto es lo que imprime:

# Abcd
# salida

# Prueba algunos ejemplos más avanzados y verifíca su salida:

print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
    # Abcd
    # Alpha 
    # Alpha 
    #  alpha
    # 123
    # Αβγδ