
"""Algunas excepciones útiles"""
# Analicemos con más detalle algunas excepciones útiles (o más bien, las más comunes) que puedes llegar a experimentar.

ZeroDivisionError
# Esta aparece cuando intentas forzar a Python a realizar cualquier operación que provoque una división en la que el divisor es cero o no se puede distinguir de cero. Toma en cuenta que hay más de un operador de Python que puede hacer que se genere esta excepción. ¿Puedes adivinarlos todos?

# Si, estos son: /, //, y %.

ValueError
# Espera esta excepción cuando estás manejando valores que pueden usarse de manera inapropiada en algún contexto. En general, esta excepción se genera cuando una función (como int() o float()) recibe un argumento de un tipo adecuado, pero su valor es inaceptable.

TypeError
# Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual. Mira el ejemplo:

short_list = [1]
# one_value = short_list[0.5]

# No está permitido usar un valor flotante como índice de una lista (la misma regla también se aplica a las tuplas). TypeError es un nombre adecuado para describir el problema y una excepción adecuada a generar.

AttributeError
# Esta excepción llega, entre otras ocasiones, cuando intentas activar un método que no existe en un elemento con el que se está tratando. Por ejemplo:

short_list = [1]
short_list.append(2)
short_list.depend(3)

# La tercera línea de nuestro ejemplo intenta hacer uso de un método que no está incluido en las listas. Este es el lugar donde se genera la excepción AttributeError.

SyntaxError
# Esta excepción se genera cuando el control llega a una línea de código que viola la gramática de Python. Puede sonar extraño, pero algunos errores de este tipo no se pueden identificar sin ejecutar primero el código. Este tipo de comportamiento es típico de los lenguajes interpretados: el intérprete siempre trabaja con prisa y no tiene tiempo para escanear todo el código fuente. Se conforma con comprobar el código que se está ejecutando en el momento. Muy pronto se te presentará un ejemplo de esta categoría.

# Es una mala idea manejar este tipo de excepciones en tus programas. Deberías producir código sin errores de sintaxis, en lugar de enmascarar las fallas que has causado.

