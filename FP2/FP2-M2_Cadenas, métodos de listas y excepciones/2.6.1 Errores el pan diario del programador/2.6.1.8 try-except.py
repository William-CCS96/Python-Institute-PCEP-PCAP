"""Excepciones: continuación"""
# Este enfoque tiene una desventaja importante: si existe la posibilidad de que más de una excepción se salte a un apartado except:, puedes tener problemas para descubrir lo que realmente sucedió.

# Al igual que en el código en el editor. Ejecútalo y ve lo que pasa.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")


# El mensaje: Oh cielos, algo salio mal... que aparece en la consola no dice nada acerca de la razón, mientras que hay dos posibles causas de la excepción:

    # Datos no enteros fueron ingresados por el usuario.
    # Un valor entero igual a 0 fue asignado a la variable x.

# Técnicamente, hay dos formas de resolver el problema:

#     # Construir dos bloques consecutivos try-except, uno por cada posible motivo de excepción (fácil, pero provocará un crecimiento desfavorable del código).
#     # Emplear una variante más avanzada de la instrucción.
# Se ve de la siguiente manera:

# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :


# Así es como funciona:

#         Si el try genera la excepción exc1, esta será manejada por el bloque except exc1:.
#         De la misma manera, si el try genera la excepción exc2, esta será manejada por el bloque except exc2:.
#         Si el try genera cualquier otra excepción, será manejado por el bloque sin nombre except.
# Pasemos a la siguiente parte del curso y veámoslo en acción.

