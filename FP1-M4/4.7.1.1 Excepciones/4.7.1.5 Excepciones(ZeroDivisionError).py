
# Cómo lidiar con más de una excepción
# La respuesta obvia es "no": hay más de una forma posible de plantear una excepción. Por ejemplo, un usuario puede ingresar cero como entrada, ¿puedes predecir lo que sucederá a continuación?

# Sí, tienes razón: la división colocada dentro de la invocación de la función print() generará la excepción ZeroDivisionError. Como es de esperarse, el comportamiento del código será el mismo que en el caso anterior: el usuario verá el mensaje "No se que hacer con...", lo que parece bastante razonable en este contexto, pero también es posible que desees manejar este tipo de problema de una manera un poco diferente.

# ¿Es posible? Por supuesto que lo es. Hay al menos dos enfoques que puedes implementar aquí.

# El primero de ellos es simple y complicado al mismo tiempo: puedes agregar dos bloques try por separado, uno que incluya la invocación de la función input() donde se puede generar la excepción ValueError, y el segundo dedicado a manejar posibles problemas inducidos por la división. Ambos bloques try tendrían su propio except, y de esa manera, tendrías un control total sobre dos errores diferentes.

# Esta solución es buena, pero es un poco larga: el código se hincha innecesariamente. Además, no es el único peligro que te espera. Toma en cuenta que dejar el primer bloque try-except deja mucha incertidumbre; tendrás que agregar código adicional para asegurarte de que el valor que ingresó el usuario sea seguro para usar en la división. Así es como una solución aparentemente simple se vuelve demasiado complicada.

# Afortunadamente, Python ofrece una forma más sencilla de afrontar este tipo de desafíos.

# Dos excepciones después de un try.
# Observa el código.

# Como puedes ver, acabamos de agregar un segundo except. Esta no es la única diferencia; toma en cuenta que ambos except tienen nombres de excepción específicos. En esta variante, cada una de las excepciones esperadas tiene su propia forma de manejar el error, pero se debe enfatizarse en que solo una de todas puede interceptar el control; si se ejecuta una, todas las demás permanecen inactivas. Además, la cantidad de excepciones no está limitado: puedes especificar tantas o tan pocas como necesites, pero no se te olvide que ninguna de las excepciones se puede especificar más de una vez.

# Pero esta todavía no es la última palabra de Python sobre excepciones.

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')  
