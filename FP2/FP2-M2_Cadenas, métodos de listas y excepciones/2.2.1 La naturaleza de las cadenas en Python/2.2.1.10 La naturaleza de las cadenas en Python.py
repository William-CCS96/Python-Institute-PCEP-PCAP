"""Operaciones con cadenas: continuación"""
# No pienses que la inmutabilidad de una cadena limita tu capacidad de operar con ellas.
# La única consecuencia es que debes recordarlo e implementar tu código de una manera ligeramente diferente: observa el código en el editor.

# Esta forma de código es totalmente aceptable, funcionará sin doblar las reglas de Python y traerá el alfabeto latino completo a tu pantalla:

# Es posible que desees preguntar si el crear una nueva copia de una cadena cada vez que se modifica su contenido empeora la efectividad del código.
# Sí, lo hace un poco. Sin embargo, no es un problema en lo absoluto.

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)    
    # abcdefghijklmnopqrstuvwxyz