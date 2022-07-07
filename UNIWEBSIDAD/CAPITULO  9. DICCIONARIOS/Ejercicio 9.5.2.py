"""Ejercicio 9.5.2. Diccionarios usados para contar."""
import random

# Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

cadena="Qué lindo día que hace hoy"

def stri_to_dicc(string):
    string=string.lower()
    conv_string=normalize(string)
    dicci={}
    word=""
    count=0

    for letter in conv_string:
        if letter==" ":
            if len(word)>0:
                count=conv_string.count(word)
                dicci[word]=count
                word=""
                count=0
        else:word+=letter
    return dicci

print(stri_to_dicc(cadena))
    # {'qué': 1, 'lindo': 1, 'día': 1, 'que': 1, 'hace': 1}

# Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario

cadena="Qué lindo día que hace hoy"

def letter_coun_to_dicc(string):
    string=string.lower()
    conv_string=normalize(string)
    dicci={}
    count=0
    for letter in conv_string:
        if letter!=" ":
            count=conv_string.count(letter)
            dicci[letter]=count
            count=0
        else:continue
    return dicci

print(letter_coun_to_dicc(cadena))
    # {'q': 2, 'u': 2, 'e': 3, 'l': 1, 'i': 2, 'n': 1, 'd': 2, 'o': 2, 'a': 2, 'h': 2, 'c': 1, 'y': 1}

# Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados. Nota: utilizar el módulo random para obtener tiradas aleatorias.


def count_tiros(range_random):
    list_dados=[]
    dicci={}
    count=random.randint(2,range_random)
    for i in range(count):
        dado1=random.randint(0,6)
        dado2=random.randint(0,6)
        list_dados.append([dado1,dado2])
    print(list_dados)
    new_list=[]
    sumato=0
    for i in range(len(list_dados)):
        sumato=list_dados[i][0] +list_dados[i][1]
        new_list.append(sumato)
    print(new_list)
    for i in new_list:
        dicci[i]=new_list.count(i)
    return f"Los lanzamientos son: {list_dados}\nLa sumatoría de los lanzamientos es: {new_list}\nLa cantidad de resultados es: {dicci}"
    

    
print(count_tiros(10))
[[3, 5], [6, 6], [4, 6], [0, 2], [0, 4], [2, 6], [2, 5], [2, 0], [2, 3], [4, 5]]
[8, 12, 10, 2, 4, 8, 7, 2, 5, 9]
{8: 2, 12: 1, 10: 1, 2: 2, 4: 1, 7: 1, 5: 1, 9: 1}

# Los lanzamientos son: [[3, 6], [1, 0], [1, 2], [4, 0], [2, 6], [4, 4], [6, 0], [3, 0], [6, 5], [6, 2]]
# La sumatoría de los lanzamientos es: [9, 1, 3, 4, 8, 8, 6, 3, 11, 8]
# La cantidad de resultados es: {9: 1, 1: 1, 3: 2, 4: 1, 8: 3, 6: 1, 11: 1}