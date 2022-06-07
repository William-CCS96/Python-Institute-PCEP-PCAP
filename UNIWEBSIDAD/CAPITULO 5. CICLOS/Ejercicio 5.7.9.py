# Ejercicio 5.7.9. Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

# Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.
# Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?

def nums_multiplos1(a,b):
    count=0
    if a==0:
        return print("El primer número debe ser distinco de cero")
    if a<b:
        for x in range(b):
            if x==0:
                continue
            elif (a*x)<b:
                count+=1
            else:
                break
    else: 
        return print("El primer número no puede ser mayor que el segundo")
    print("La cantidad de multiplos del número",a,"menores que el número",b,"son:", count)

nums_multiplos1(3,17)

def nums_multiplos2(a,b):
    count=0
    if a==0:
        return print("El primer número debe ser distinco de cero")
    if a<b:
        while True:
            if (a*(count+1))<b:
                count+=1
                continue
            else:
                break
    else: 
        return print("El primer número no puede ser mayor que el segundo")
    print("La cantidad de multiplos del número",a,"menores que el número",b,"son:", count)

nums_multiplos2(3,1245)