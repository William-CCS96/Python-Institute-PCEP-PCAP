"""Tu primer módulo: paso 7"""
# Este módulo contendrá dos funciones simples, y si deseas saber cuantas veces se han invocado las funciones, necesitas un contador inicializado en cero cuando se importe el módulo.

# Puedes hacerlo de esta manera:

counter = 0

if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")

"""Tu primer módulo: paso 8"""
# El introducir tal variable es absolutamente correcto, pero puede causar importantes efectos secundarios que debes tomar en cuenta.

# Analiza el archivo modificado main.py:

import module
print(module.counter)

# Como puedes ver, el archivo principal intenta acceder a la variable de contador del módulo. ¿Es esto legal? Sí lo es. ¿Es utilizable? Claro. ¿Es seguro?

# Eso depende: si confías en los usuarios de tu módulo, no hay problema; sin embargo, es posible que no desees que el resto del mundo vea tu variable personal o privada.

# A diferencia de muchos otros lenguajes de programación, Python no tiene medios para permitirte ocultar tales variables a los ojos de los usuarios del módulo.

# Solo puedes informar a tus usuarios que esta es tu variable, que pueden leerla, pero que no deben modificarla bajo ninguna circunstancia.

# Esto se hace anteponiendo al nombre de la variable _ (un guión bajo) o __ (dos guiones bajos), pero recuerda, es solo un acuerdo. Los usuarios de tu módulo pueden obedecerlo o no.

# Nosotros por supuesto, lo respetaremos. Ahora pongamos dos funciones en el módulo: evaluarán la suma y el producto de los números recopilados en una lista.

# Además, agreguemos algunos adornos allí y eliminemos los restos superfluos.

"""Tu primer módulo: paso 9"""
# Bueno. Escribamos un código nuevo en nuestro archivo module.py. El módulo actualizado está listo aquí:

#!/usr/bin/env python3 

""" module.py - Un ejemplo de un módulo en Python """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

# Algunos elementos necesitan explicación:

        # La línea que comienza con #! tiene muchos nombres - puede ser llamada shabang, shebang, hashbang, poundbang o incluso hashpling (no nos preguntes por qué). El nombre en sí no significa nada aquí, su papel es más importante. Desde el punto de vista de Python, es solo un comentario debido a que comienza con #. Para sistemas operativos Unix y similares a Unix (incluido MacOS), dicha línea indica al sistema operativo como ejecutar el contenido del archivo (en otras palabras, que programa debe ejecutarse para interpretar el texto). En algunos entornos (especialmente aquellos conectados con servidores web) la ausencia de esa línea causará problemas.
        # Una cadena (quizás una multilínea) colocada antes de las instrucciones de cualquier módulo (incluidas las importaciones) se denomina doc-string, y debe explicar brevemente el propósito y el contenido del módulo.
        # Las funciones definidas dentro del módulo (suml() y prodl()) están disponibles para ser importadas.
        # Se ha utilizado la variable __name__ para detectar cuando se ejecuta el archivo de forma independiente, y se aprovechó esta oportunidad para realizar algunas pruebas sencillas.
        
"""Tu primer módulo: paso 10"""
# Ahora es posible usar el nuevo módulo, esta es una forma de hacerlo:

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
