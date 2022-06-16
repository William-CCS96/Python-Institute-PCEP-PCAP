"""Excepciones: continuación"""
# No olvides que:

    # Los bloques except son analizados en el mismo orden en que aparecen en el código.
    # No debes usar más de un bloque de excepción con el mismo nombre.
    # El número de diferentes bloques except es arbitrario, la única condición es que si se emplea el try, debes poner al menos un except (nombrado o no) después de el.
    # La palabra clave reservada except no debe ser empleada sin que le preceda un try.
    # Si uno de los bloques except es ejecutado, ningún otro lo será.
    # Si ninguno de los bloques except especificados coincide con la excepción planteada, la excepción permanece sin manejar (lo discutiremos pronto).
    # Si un except sin nombre existe, tiene que especificarse como el último.
# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :


# Continuemos ahora con los experimentos.
# Observa el código en el editor. Hemos modificado el programa anterior, hemos eliminado el bloque ZeroDivisionError.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")

# ¿Qué sucede ahora si el usuario ingresa un 0 como entrada?
# Como no existe un bloque declarado para la división entre cero, la excepción cae dentro del bloque general (sin nombre): esto significa que en este caso, el programa dirá:

        # Oh cielos, algo salió mal...
        # FIN.




