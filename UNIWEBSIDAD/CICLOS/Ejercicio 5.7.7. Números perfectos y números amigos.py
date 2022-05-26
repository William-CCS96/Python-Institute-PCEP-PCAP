# Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.

# Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).

# Usando la primera función, escribir una función que imprima las primeras m parejas de números (a,b), tales que la suma de los divisores de a es igual a b y la suma de los divisores de b es igual a a (es decir las primeras m parejas de números amigos).

# Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.

def divisores(num):
    num_divisores=[]
    x=1
    while True:
        if num==1:
            num_divisores=[1]
            break
        if num==x:
            break
        if num%x==0:
            num_divisores.append(x)
        x+=1
    return num_divisores




def num_perfect(m):
    x=1
    list_perfect=[]
    count=0
    while True:
        if count==m:
            break
        if (x%3==0 or x%5==0)and(x!=6 and x!=3):
            x+=1
            continue
        if len(divisores(x))==1:
            x+=1
            continue
        perfect=0
        for i in divisores(x):
            perfect+=i
        if perfect==x:
            list_perfect.append(x)
            count+=1
            perfect=0
            x+=1
        else:
            x+=1
    print(list_perfect) 

num_perfect(5)








# Ejercicio 5.7.8. Escribir un programa que le pida al usuario que ingrese una sucesión de núme-ros naturales (primero uno, luego otro, y así hasta que el usuario ingrese -1 como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

# Ejercicio 5.7.9. Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

# Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.
# Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
# Ejercicio 5.7.10. Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.

# Ejercicio 5.7.11. Escribir una función que reciba un dígito y un número natural, y decida numéricamente si el dígito se encuentra en la notación decimal del segundo.

# Ejercicio 5.7.12. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

