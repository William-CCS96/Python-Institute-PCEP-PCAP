#METODO     es una función que es especial para un tipo de dato en particular

#FUNCIONES INTEGRADAS:
"""https://docs.python.org/3/library/functions.html"""


#upper() cambia todos los caracteres a mayuscula
nombre=input("¿Cuál es tu nombre?")
nombre=nombre.upper()
        # WILLIAM

#capitalize() Cambia el primer caracteren mayuscula
nombre=nombre.capitalize()
        # Camilo

#strip() Eliminar los espacios 
nombre=nombre.strip()

#lower() Cambia todos los caracteres a miniscula
nombre=nombre.lower()

#replace() Recibe caractares,el primero es elcaracter a buscar y el segundo por el que se reemplaz
nombre=nombre.replace("o","a")
    #camila

#Acceder a un caracter en especial
print(nombre[2])
    #m

#Saber que tan largo es un string
print(len(nombre))
    #6
