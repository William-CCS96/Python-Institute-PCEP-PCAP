"""Excepciones: continuación"""
# Si deseas manejar dos o más excepciones de la misma manera, puedes usar la siguiente sintaxis:

# try:
#     :
# except (exc1, exc2):
#     :

# Simplemente tienes que poner todos los nombres de las excepciones empleadas en una lista separada por comas y no olvidar los paréntesis.

# Si una excepción es generada dentro de una función, puede ser manejada:

        # Dentro de la función.
        # Fuera de la función.
# Comencemos con la primera variante: observa el código en el editor.
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema Aritmético!")
    return None

bad_fun(0)

print("FIN.")
# La excepción ZeroDivisionError (la cual es un caso concreto de la clase ArithmeticError) es generada dentro de la función badfun(), y la función en sí misma se encarga de ella.

# La salida del programa es:
        # ¡Problema Aritmético!
        # FIN.

# También es posible dejar que la excepción se propague fuera de la función. Probémoslo ahora.
# Observa el código a continuación:

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se generó una excepción!")

print("FIN.")

# El problema tiene que ser resuelto por el invocador (o por el invocador del invocador, y así sucesivamente).
# La salida del programa es:
        # ¿Qué pasó? ¡Se generó una excepción!
        # FIN.

# Nota: la excepción generada puede cruzar la función y los límites del módulo, y viajar a través de la cadena de invocación buscando una cláusula except capaz de manejarla.

# Si no existe tal cláusula, la excepción no se controla y Python resuelve el problema de la manera estándar - terminando el código y emitiendo un mensaje de diagnóstico.

