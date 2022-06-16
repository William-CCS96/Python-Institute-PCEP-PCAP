"""Excepciones: continuación"""
# Observa el código en el editor. Es un ejemplo simple para comenzar. Ejecútalo.
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuupsss...")

print("FIN.")
    # Uuuppsss...
    # FIN.

# Ahora observa el código a continuación:
try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.")
    # Uuuppsss...
    # FIN.  

# Algo ha cambiado: hemos reemplazado ZeroDivisionError con ArithmeticError.
# Ya se sabe que ArithmeticError es una clase general que incluye (entre otras) la excepción ZeroDivisionError.

# Por lo tanto, la salida del código permanece sin cambios. Pruébalo.
# Esto también significa que reemplazar el nombre de la excepción ya sea con Exception o BaseException no cambiará el comportamiento del programa.


# Vamos a resumir:
#     Cada excepción generada cae en la primer coincidencia.
#     La coincidencia correspondiente no tiene que especificar exactamente la misma excepción, es suficiente que la excepción sea más general (más abstracta) que la generada.
