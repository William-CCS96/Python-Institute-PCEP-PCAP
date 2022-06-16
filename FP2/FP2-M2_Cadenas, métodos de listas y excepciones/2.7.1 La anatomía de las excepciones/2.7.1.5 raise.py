"""Excepciones: continuación"""
# La instrucción raise genera la excepción especificada denominada exc como si fuese generada de manera natural:

# raise exc

# Nota: raise es una palabra clave reservada.

# La instrucción te permite:

        # Simular excepciones reales (por ejemplo, para probar tu estrategia de manejo de excepciones).
        # Parcialmente manejar una excepción y hacer que otra parte del código sea responsable de completar el manejo.
# Observa el código en el editor. Así es como puedes usarlo en la práctica.

# La salida del programa permanece sin cambios.

# De esta manera, puedes probar tu rutina de manejo de excepciones sin forzar al código a hacer cosas incorrectas.

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")
