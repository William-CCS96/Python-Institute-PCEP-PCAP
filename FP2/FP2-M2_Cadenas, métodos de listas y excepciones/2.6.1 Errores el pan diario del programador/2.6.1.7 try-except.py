"""Excepciones: continuación"""
# Observa el código en el editor. Te ayudará a comprender este mecanismo.

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salió mal...")

print("3")

# Esta es la salida que produce:

# 1
# Oh cielos, algo salió mal...
# 3

# Nota: la instrucción print("2") se perdió en el proceso.

