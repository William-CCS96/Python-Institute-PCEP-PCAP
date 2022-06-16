"""Excepciones: continuación"""
# Observa el código en el editor. Este es el enfoque favorito de Python.

# Nota:

# La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
# Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
# La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal: si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de la palabra clave reservada except debería proporcionar una reacción adecuada a la excepción planteada.
# Por ultimo, se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.
# Ejecuta el código y prueba su comportamiento.


# Resumamos esto:

# try:
#     :
#     :
# except:
#     :
#     :


# En el primer paso, Python intenta realizar todas las instrucciones colocadas entre las instrucciones try: y except:.
# Si no hay ningún problema con la ejecución y todas las instrucciones se realizan con éxito, la ejecución salta al punto después de la última línea del bloque except: , y la ejecución del bloque se considera completa.
# Si algo sale mal dentro del bloque try: o except:, la ejecución salta inmediatamente fuera del bloque y entra en la primera instrucción ubicada después de la palabra clave reservada except:, esto significa que algunas de las instrucciones del bloque pueden ser silenciosamente omitidas.

first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")
