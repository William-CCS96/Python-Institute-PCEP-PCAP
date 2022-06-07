# Cuando los datos no son lo que deberían ser

# Escribamos un fragmento de código extremadamente trivial: leerá un número natural (un entero no negativo) e imprimirá su recíproco. De esta forma, 2 se convertirá en 0.5 (1/2) y 4 en 0.25 (1/4). Aquí está el programa

value = int(input('Ingresa un número natural: '))
print('El recíproco de', value, 'es', 1/value)
# Parece que ya sabes hacia dónde vamos. Sí, tienes razón: ingresar datos que no sean un número entero (que también incluye ingresar nada) arruinará completamente la ejecución del programa. Esto es lo que verá el usuario del código:

"""Traceback (most recent call last):
  File "code.py", line 1, in 
    value = int(input('Ingresa un número natural: '))
ValueError: invalid literal for int() with base 10: ''"""
        # La primera palabra de la línea es el nombre de la excepción la cual provoca que tu código se detenga. Su nombre aquí es ValueError

# Ya deberías poder implementar esta verificación y escribirla tu mismo, ¿no es así? También es posible comprobar si la variable value es de tipo int (Python tiene un medio especial para este tipo de comprobaciones: es un operador llamado is. La revisión en sí puede verse de la siguiente manera:

type(value) is int  
    # Su resultado es verdadero si el valor actual de la variable value es del tipo int.