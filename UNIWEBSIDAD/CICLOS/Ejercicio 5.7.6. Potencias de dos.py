# Ejercicio 5.7.6. Potencias de dos.

# Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.

# Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos, descripta en el punto anterior.


from importlib import import_module


num=int(input("Introduce el número: "))

def es_potencia_de_dos(num):
    x=1
    validar=False
    while True:
        if num==2**x: 
            validar=True
            break
        elif num!=2**x and num>=2**x:
            x+=1
        else:
            break
    return validar



def suma_potencias(x,y):
    if x==y:
        print("los números no pueden ser iguales")
        return 0
    mayor=max(x,y)
    menor=min(x,y)
    correct=[]
    count=1
    if es_potencia_de_dos(menor):
            correct.append(menor)
    if es_potencia_de_dos(mayor):
            correct.append(mayor)
    while True:
        if es_potencia_de_dos(menor+count)and menor+count<mayor:
            correct.append(menor+count)
            count+=1
        elif menor+count==mayor:
            break
        else:
            count+=1
        if menor+count==mayor:
            break
    sumatoria=0
    if len(correct)==0:
        return 0
    elif len(correct)==1:
        sumatoria=correct[0]
        return sumatoria
    for i in range(len(correct)):
        sumatoria+=correct[i]
    return sumatoria


x=int(input("Indica el primer número: "))
y=int(input("Indica el segundo número: "))
print(suma_potencias(x,y))