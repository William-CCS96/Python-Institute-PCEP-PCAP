"""Funciones seleccionadas del módulo random: continuación"""
# Las funciones anteriores tienen una desventaja importante: pueden producir valores repetidos incluso si el número de invocaciones posteriores no es mayor que el rango especificado.

# Observa el código en el editor. Es muy probable que el programa genere un conjunto de números en el que algunos elementos no sean únicos.

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')


# Esto es lo que se obtuvo al ejecutarlo:

    # 9,4,5,4,5,8,9,4,8,4,


"""Las funciones choice y sample"""
# Como puedes ver, esta no es una buena herramienta para generar números para la lotería. Afortunadamente, existe una mejor solución que escribir tu propio código para verificar la singularidad de los números "sorteados".


# Es una función con el nombre de choice:

        # choice(secuencia)
        # sample(secuencia, elementos_a_elegir=1)
# La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.

# El segundo crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) "sorteado" de la secuencia de entrada.

# En otras palabras, la función elige algunos de los elementos de entrada, devolviendo una lista con la elección. Los elementos de la muestra se colocan en orden aleatorio. Nota que elementos_a_elegir no debe ser mayor que la longitud de la secuencia de entrada.

# Observa el código a continuación:

from random import choice, sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

# Nuevamente, la salida del programa no es predecible. Nuestros resultados se ven así:

        # 4
        # [3, 1, 8, 9, 10]
        # [10, 8, 5, 1, 6, 4, 3, 9, 7, 2]