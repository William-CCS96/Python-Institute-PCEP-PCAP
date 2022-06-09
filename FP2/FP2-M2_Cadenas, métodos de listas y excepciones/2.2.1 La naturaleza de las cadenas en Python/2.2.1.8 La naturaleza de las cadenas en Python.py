"""Los operadores in y not in"""
# El operador in

# El operador in no debería sorprenderte cuando se aplica a cadenas, simplemente comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).

# El resultado es simplemente True(Verdadero) o False(Falso).

# Observa el ejemplo a continuación. Así es como el operador in funciona:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
    # True
    # False
    # False
    # True
    # False
"""
El operador not in"""

# Como probablemente puedas deducir, el operador not in también es aplicable aquí.
# Así es como funciona:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)
    # False
    # True
    # True
    # False
    # True