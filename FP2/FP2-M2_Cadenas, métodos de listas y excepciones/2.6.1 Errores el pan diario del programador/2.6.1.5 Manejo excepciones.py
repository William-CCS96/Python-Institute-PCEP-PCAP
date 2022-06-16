"""Excepciones: continuación"""
# ¿Cómo se manejan las excepciones? La palabra try es clave para la solución.

# Además, también es una palabra clave reservada.

# La receta para el éxito es la siguiente:

# Primero, se debe intentar (try) hacer algo.
# Después, tienes que comprobar si todo salió bien.
# Pero, ¿no sería mejor verificar primero todas las circunstancias y luego hacer algo solo si es seguro?

# Justo como el ejemplo en el editor.

first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("Esta operación no puede ser realizada.")

print("FIN.")

# Es cierto que esta forma puede parecer la mas natural y comprensible, pero en realidad, este método no facilita la programación. Todas estas revisiones pueden hacer al código demasiado grande e ilegible.
# Python prefiere un enfoque completamente diferente.

