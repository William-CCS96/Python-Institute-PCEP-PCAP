
# ¿Cómo utilizar un diccionario? El método keys()
# ¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?

        # No y si.

# No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.

# Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre el diccionario y una entidad secuencial temporal).

# El primero de ellos es un método denominado keys(), el cual es parte de todo diccionario. El método retorna o regresa una lista de todas las claves dentro del diccionario. Al tener una lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
    # gato -> chat
    # perro -> chien
    # caballo -> cheval
        
    # }La función sorted()
    # ¿Deseas que la salida este ordenada? Solo hay que agregar al bucle for lo siguiente:
for key in sorted(dictionary.keys()):

# La función sorted() hará su mejor esfuerzo y la salida será la siguiente:

    # caballo -> cheval
    # gato -> chat
    # perro -> chien

dct={}
dct["1"]=(1,2)
dct["2"]=(2,1)

for x in dct.keys():
    print(dct[x][1],end="")