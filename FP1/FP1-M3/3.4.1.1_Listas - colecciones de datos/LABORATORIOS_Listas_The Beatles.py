# Escenario
# Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

# La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

# Paso 1: Crea una lista vacía llamada beatles.
# Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
# Paso 3: Emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
# Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?)

# # paso 1
# print("Paso 1:", Beatles)
# # paso 2
# print("Paso 2:", Beatles)
# # paso 3
# print("Paso 3:", Beatles)
# # paso 4
# print("Paso 4:", Beatles)
# # paso 5
# print("Paso 5:", Beatles)

# # probando la longitud de la lista
# print("Los Fav", len(Beatles))

#Paso1:
beatles=[]
print("Paso 1: ", beatles)
    # Paso 1:  []
#Paso2:
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2: ",beatles)
    # Paso 2:  ['John Lennon', 'Paul McCartney', 'George Harrison']
#Paso3:
for i in beatles:
    if i=="George Harrison":
        beatles.append(input("Agrega los nuevos artistas 1"))
        beatles.append(input("Agrega los nuevos artistas 2"))
print("Paso 3: ", beatles)
    # Paso 3:  ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe', 'Pete Best']
#Paso4:
del((beatles[-1]))
del((beatles[-1]))
#Paso5:
print("Paso 5: ",beatles) 
