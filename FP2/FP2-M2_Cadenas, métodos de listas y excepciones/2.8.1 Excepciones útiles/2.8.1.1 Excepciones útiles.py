"""Excepciones integradas"""
# Te mostraremos una breve lista de las excepciones más útiles. Si bien puede sonar extraño llamar "útil" a una cosa o un fenómeno que es un signo visible de una falla o retroceso, como sabes, errar es humano y si algo puede salir mal, saldrá mal.

# Las excepciones son tan rutinarias y normales como cualquier otro aspecto de la vida de un programador.

# Para cada excepción, te mostraremos:

# Su nombre.
# Su ubicación en el árbol de excepciones.
# Una breve descripción.
# Un fragmento de código conciso que muestre las circunstancias en las que se puede generar la excepción.
# Hay muchas otras excepciones para explorar: simplemente no tenemos el espacio para revisarlas todas aquí.

"""ArithmeticError"""
# Ubicación: BaseException ← Exception ← ArithmeticError

# Descripción: una excepción abstracta que incluye todas las excepciones causadas por operaciones aritméticas como división cero o dominio inválido de un argumento.

"""AssertionError"""
# Ubicación: BaseException ← Exception ← AssertionError

# Descripción: una excepción concreta generada por la instrucción assert cuando su argumento se evalúa a False (falso), None (ninguno), 0, o una cadena vacía.

# Código:
from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# Debemos estar seguros de que angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))

"""BaseException"""
# Ubicación: BaseException

# Descripción: la excepción más general (abstracta) de todas las excepciones de Python: todas las demás excepciones se incluyen en esta; se puede decir que las siguientes dos excepciones son equivalentes: except: y except BaseException:.

"""IndexError"""
# Ubicación: BaseException ← Exception ← LookupError ← IndexError

# Descripción: una excepción concreta que surge cuando se intenta acceder al elemento de una secuencia inexistente (por ejemplo, el elemento de una lista).

# Código:

# El codigo muestra una forma extravagante
# de dejar el bucle.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Listo')

"""KeyboardInterrupt"""
# Ubicación: BaseException ← KeyboardInterrupt

# Descripción: una excepción concreta que surge cuando el usuario usa un atajo de teclado diseñado para terminar la ejecución de un programa (Ctrl-C en la mayoría de los Sistemas Operativos); si manejar esta excepción no conduce a la terminación del programa, el programa continúa su ejecución.

# Nota: esta excepción no se deriva de la clase Exception. Ejecuta el programa en IDLE.

# Código:

# Este código no puede ser terminado
# presionando Ctrl-C.

"""from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")"""

"""LookupError"""
# Ubicación: BaseException ← Exception ← LookupError

# Descripción: una excepción abstracta que incluye todas las excepciones causadas por errores resultantes de referencias no válidas a diferentes colecciones (listas, diccionarios, tuplas, etc.).


"""MemoryError"""
# Ubicación: BaseException ← Exception ← MemoryError
# Descripción: se genera una excepción concreta cuando no se puede completar una operación debido a la falta de memoria libre.

# Código:

    # Este código causa la excepción MemoryError.
    # Advertencia: el ejecutar este código puede afectar tu Sistema Operativo.
    # ¡No lo ejecutes en entornos de producción!

"""string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')"""

"""OverflowError"""
# Ubicación: BaseException ← Exception ← ArithmeticError ← OverflowError
# Descripción: una excepción concreta que surge cuando una operación produce un número demasiado grande para ser almacenado con éxito.

# Código:

# El código imprime los valores subsequentes
# de exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')

"""ImportError"""
# Ubicación: BaseException ← Exception ← StandardError ← ImportError
# Descripción: se genera una excepción concreta cuando falla una operación de importación.
# Código:

# Una de estas importaciones fallará, ¿cuál será?

try:
    import math
    import time
    import abracadabra

except:
    print('Una de tus importaciones ha fallado.')

"""KeyError"""
# Ubicación: BaseException ← Exception ← LookupError ← KeyError
# Descripción: una excepción concreta que se genera cuando intentas acceder al elemento inexistente de una colección (por ejemplo, el elemento de un diccionario).
# Código:

# ¿Cómo abusar del diccionario
# y cómo lidiar con ello?

dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)

"""REVISAR BIBLIOGRAFÍA DE EXCEPCIONES:
    https://docs.python.org/3.6/library/exceptions.html"""