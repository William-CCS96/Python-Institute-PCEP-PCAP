# Ejercicio 5.7.2. Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.


number=int(input("Ingresa el número entero a descomponer:"))
descomp=[]
x=2
while True:
    if number==x:
        descomp.append(x)
        break
    if number%x==0:
        descomp.append(x)
        number/=x
    if number%x!=0:
        x=x+1

print(descomp)
