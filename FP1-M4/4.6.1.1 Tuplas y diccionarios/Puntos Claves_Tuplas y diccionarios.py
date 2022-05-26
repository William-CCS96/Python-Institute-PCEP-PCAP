# Ejercicio 1
# ¿Qué ocurrirá cuando se intente ejecutar el siguiente código?
my_tup = (1, 2, 3)
print(my_tup[2])
    # 3
    
#-------------------------------------------
# Ejercicio 2
# ¿Cuál es la salida del siguiente fragmento de código?
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)
    # 6 
    # El programa imprimirá 6 en pantalla. Los elementos de la tupla tup han sido "desempaquetados" en las variables a, b, y c.
    
#-------------------------------------------
# Ejercicio 3
# Completa el código para emplear correctamente el método count() para encontrar la cantidad de 2 duplicados en la tupla siguiente.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)    # salida: 4
    
#-------------------------------------------
# Ejercicio 4
# Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
    # {'Adam Smith': 'A', 'Judy Paxton': 'B+', 'Mary Louis': 'A', 'Patrick White': 'C'}
    
#-------------------------------------------
# Ejercicio 5
# Escribe un programa que convierta la lista my_list en una tupla.

my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)
    # ('car', 'Ford', 'flower', 'Tulip')

    
#-------------------------------------------
# Ejercicio 6
# Escribe un programa que convierta la tupla colors en un diccionario.

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)
    # {'green': '#008000', 'blue': '#0000FF'}
    
#-------------------------------------------
# Ejercicio 7
# ¿Que ocurrirá cuando se ejecute el siguiente código?

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)
    # {'A': 1, 'B': 2}

#-------------------------------------------
# Ejercicio 8
# ¿Cuál es la salida del siguiente programa?

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
    # blanco : (255, 255, 255)
    # gris : (128, 128, 128)
    # rojo : (255, 0, 0)
    # verde : (0, 128, 0)