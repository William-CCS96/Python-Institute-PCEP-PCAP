# Ejercicio 4.6.1. Escribir funciones que resuelvan los siguientes problemas:

# Dado un número entero n, indicar si es o no par.
# Dado un número entero n, indicar si es o no primo.


def par_prime(n):
    if n%2==0: print("El número",n,"es par")
    else:print("El número",n,"es impar")
    x=2
    while True:
        if n==1:
            print("El número",n,"no es primo")
            break
        if n==x:
            print("El número",n,"si es primo") 
            break
        if n%x!=0:x+=1
        else:
            print ("El número",n,"no es primo")
            break
par_prime(6)