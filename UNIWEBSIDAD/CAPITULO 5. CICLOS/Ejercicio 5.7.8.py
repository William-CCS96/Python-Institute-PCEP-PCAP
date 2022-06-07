# Ejercicio 5.7.8. Escribir un programa que le pida al usuario que ingrese una sucesión de núme-ros naturales (primero uno, luego otro, y así hasta que el usuario ingrese -1 como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

def num_print():
    list_num=[]
    adding=0
    while True:
        try:
            num=int(input("Ingresa un número ó -1 para conocer la suma y el promedio: "))
        except ValueError:
            print("Ingresa un valor valido")
            continue
        if num==-1:
            if len(list_num)==0:
                print("Vuelve pronto")
                return
            if len(list_num)==1:
                print("Por favor indica más valores")
                continue
            else:
                break
        list_num.append(num)
    for i in list_num:
        adding+=i
    print("\nIngresaste",len(list_num), "números:",list_num)
    print("la suma de los números ingresados es igual a:",adding)
    print("El promedio de los números ingresados es:",round((adding/len(list_num)),2))

num_print()

# Ingresa un número ó -1 para conocer la suma y el promedio: f
# Ingresa un valor valido
# Ingresa un número ó -1 para conocer la suma y el promedio: 5
# Ingresa un número ó -1 para conocer la suma y el promedio: f
# Ingresa un valor valido
# Ingresa un número ó -1 para conocer la suma y el promedio: 6
# Ingresa un número ó -1 para conocer la suma y el promedio: -1

# Ingresaste 2 números: [5, 6]
# la suma de los números ingresados es igual a: 11
# El promedio de los números ingresados es: 5.5