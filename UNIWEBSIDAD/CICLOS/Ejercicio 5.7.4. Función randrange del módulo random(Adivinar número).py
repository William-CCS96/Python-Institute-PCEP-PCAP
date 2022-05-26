# Ejercicio 5.7.4. Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique sin son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.
import random

x=random.randint(1,100)
print("El número secreto está entre 1 y 100")
attempts=[]
while True:
    val=int(input("Ingresa el valor que crees:"))
    attempts.append(val)
    print(attempts)
    if val<1 or val>100:
        print("Indica un número valido")
    elif x==val:
        print("¡Lo lograste!")
        break
    elif val>x:
        print("Aún no aciertas")
        print("El número secreto es menor")
    elif val<x:
        print("Aún no aciertas")
        print("El número secreto es mayor")
