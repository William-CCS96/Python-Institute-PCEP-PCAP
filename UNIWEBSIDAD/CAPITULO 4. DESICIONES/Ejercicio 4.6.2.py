# Ejercicio 4.6.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

def abs(n):
    if n<0:m=n*-1
    else:m=n
    print("El valor absoluto de",n,"es:",m)
    
abs(-5)
# El valor absoluto de -5 es: 5
