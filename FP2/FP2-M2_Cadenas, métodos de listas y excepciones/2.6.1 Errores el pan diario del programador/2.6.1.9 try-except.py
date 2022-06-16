"""Excepciones: continuación"""
# Observa el código en el editor. Nuestra solución esta ahí.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")


# El código, cuando se ejecute, producirá una de las siguientes cuatro variantes de salida:

# Si se ingresa un valor entero válido distinto de cero (por ejemplo, 5) dirá:
        # 0.2
        # FIN.

# Si se ingresa 0, dirá:
        # No puedes dividir entre cero, lo siento.
        # FIN.

# Si se ingresa cualquier cadena no entera, verás:
        # Debes ingresar un valor entero.
        # FIN.

# (Localmente en tu máquina) si presionas Ctrl-C mientras el programa está esperando la entrada del usuario (provocará una excepción denominada KeyboardInterrupt), el programa dirá:
        # Oh cielos, algo salió mal...
        # FIN.


