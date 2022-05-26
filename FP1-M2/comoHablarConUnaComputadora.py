#La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.
print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")
    # Mmm... Estoy aprendiendo ...¿en serio?

# input() con un argumento
anything = input("Dime algo...")
print("Mmm...", anything, "...¿En serio?")

#Resultado de la función input()
    #el resultado de la función input() es una cadena.
    #no se debe utilizar como un argumento para operaciones matemáticas

#CONVERSION DE DATOS (casting)   
    # La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante).
    # La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).

anything = float(input("Inserta un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)
    #5.0 al cuadrado es 25.0

anything = int(input("Inserta un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)   
    #4 al cuadrado es 16.0

anything = int(input("Inserta un número: "))
something = int(anything ** 2.0)
print(anything, "al cuadrado es", something)   
    #9 al cuadrado es 81

anything = float(input("Inserta un número: "))
something = int(anything ** 2.0)
print(anything, "al cuadrado es", something)
    #8.0 al cuadrado es 64

anything = int(float(input("Inserta un número: ")))
something = anything ** 2.0
print(anything, "al cuadrado es", something)
    #3 al cuadrado es 9.0

#MÁS ACERCA DE FUNCIÓN prin(), float() , int()
leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

    #la expresión como argumento en la función print()
leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", ((leg_a**2 + leg_b**2) ** .5))


#OPERADORES DE C,ENAS - INTRODUCCIÓN

    #Concatenación
        # "+"
        #string + string
        # no es conmutativo, por ejemplo, "ab" + "ba" no es lo mismo que "ba" + "ab".
        #El utilizar + para concatenar cadenas te permite construir la salida de una manera más precisa
        
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + fnam + " " + lnam + ".")
        #Gracias.
        # 
        # Tu nombre es William  Correa.

    #Replicación
        # "*"
        # string * number
        # number * string
        # Replica la cadena el numero de veces indicado por el número.

        # "James" * 3 produce "JamesJamesJames"
        # 3 * "an" produce "ananan"
        # 5 * "2" (o "2" * 5) produce "22222" (no 10!)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


#INDICAR AL USUARIO PARA FINALIZAR EL PROGRAMA

name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")

print("\nPresiona la tecla Enter para finalizar el programa.")
input()
print("FIN.")

#input() Es una cadena

num_1 = input("Ingresa el primer número: ") # Ingresa 12
num_2 = input("Ingresa el segundo número: ") # Ingresa 21

print(num_1 + num_2) #el programa retorna 1221

#input() También se pueden multiplicar cadenas

prueba_input_mult=("Hey ")
print(prueba_input_mult*4)
    # Hey Hey Hey Hey

#RESUMEN DE SECCIÓN
x = int(input("Ingresa un número: ")) # El usuario ingresa un 2 
print(x * "5")
    #55

x = input("Ingresa un número: ") # El usuario ingresa un 2 
print(type(x))
    #<class 'str'>
