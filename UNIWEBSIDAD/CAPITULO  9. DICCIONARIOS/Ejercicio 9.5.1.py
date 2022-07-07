"""Ejercicio 9.5.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos."""

"""Por ejemplo:

l = [ ('Nola', 'don Pepito'), ('Nola', 'don Jose'), ('Buenos', 'días') ]
print tuplas_a_diccionario(l)
Deberá mostrar: { 'Nola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] """

l = [ ('Nola', 'don Pepito'), ('Nola', 'don Jose'), ('Buenos', 'días') ]
print(l)

def tuplas_a_diccionario(lis):
    dicci={lis[i][0]:[lis[i][1]] for i in range(len(lis)) }
    return dicci

print (tuplas_a_diccionario(l))
# {'Nola': ['don Jose'], 'Buenos': ['días']}
