"""Tiempo Estimado"""
# 20-25 minutos

"""Nivel de dificultad"""
# Medio

"""Objetivos"""
    # Mejorar las habilidades del alumno al trabajar con cadenas.
    # Utilizar los métodos incorporados de Python para las cadenas.
"""Escenario"""
# Ya sabes como funiona el método split(). Ahora queremos que lo pruebes.

# Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

    # Debe aceptar únicamente un argumento: una cadena.
    # Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
    # Si la cadena está vacía, la función debería devolver una lista vacía.
    # Su nombre debe ser mysplit().
# Utiliza la plantilla en el editor. Prueba tu código con cuidado.

"""Salida esperada"""
# ['Ser', 'o', 'no', 'ser', 'esa', 'es,', 'la', 'pregunta']
# ['Ser', 'o', 'no', 'ser,esa', 'es', 'la', 'pregunta']
# []
# ['abc']
# []

# def mysplit(strng):
    #
    # coloca tu código aquí
    #

# print(mysplit("Ser o no ser, esa es la pregunta"))
# print(mysplit("Ser o no ser,esa es la pregunta"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))


print("hola a todos .".split())
    # ['hola', 'a', 'todos', '.']


def mysplit(strng):
    list=[]
    cadena=""
    for char in range(len(strng)):
        if len(strng)==0:return list
        if strng[char]==" " and char==0:
            continue
        if strng[char]!=" ":
            cadena+=strng[char]
            if char==(len(strng)-1):
                list.append(cadena)
        elif strng[char]==" ":
            if len(cadena)!=0:
                list.append(cadena)
                cadena=""
    return list

x="hola a todos ."
print(mysplit(x))

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser     o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))