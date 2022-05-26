#     La excepción por defecto y cómo usarla
# El código ha cambiado de nuevo, ¿puedes ver la diferencia?

# Hemos agregado un tercer except, pero esta vez no tiene un nombre de excepción específico; podemos decir que es anónimo o (lo que está más cerca de su función real) es el por defecto. Puedes esperar que cuando se genere una excepción y no haya un except dedicado a esa excepción, esta será manejada por la excepción por defecto.

# Nota:
# ¡el except por defecto debe ser el último except! ¡Siempre!

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')