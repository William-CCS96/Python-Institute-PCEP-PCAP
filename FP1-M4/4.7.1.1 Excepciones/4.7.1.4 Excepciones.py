
# La excepción confirma la regla
# Reescribamos el código para adoptar el enfoque de Python para la vida.


# Resumamos lo que hemos hablado:

# Cualquier fragmento de código colocado entre try y except se ejecuta de una manera muy especial: cualquier error que ocurra aquí dentro no terminará la ejecución del programa. En cambio, el control saltará inmediatamente a la primera línea situada después de la palabra clave reservada except, y no se ejecutará ninguna otra línea del bloque try.
# El código en el bloque except se activa solo cuando se ha encontrado una excepción dentro del bloque try. No hay forma de llegar por ningún otro medio.
# Cuando el bloque try o except se ejecutan con éxito, el control vuelve al proceso normal de ejecución y cualquier código ubicado más allá en el archivo fuente se ejecuta como si no hubiera pasado nada.


# Ahora queremos hacerte una pregunta: ¿Es ValueError la única forma en que el control podría caer dentro del bloque except?
# ¡Analiza el código cuidadosamente y piensa en tu respuesta!
try: # try//tratar internar

    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except:
    print('No se que hacer con', value)
