# Ejercicio 5.7.5. Algoritmo de Euclides

# Implementar en python el algoritmo de Euclides para calcular el máximo común divisor de dos números n y m, dado por los siguientes pasos.

# Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
# Si r es cero, n es el mcd de los valores iniciales.
# Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
# Hacer un seguimiento del algoritmo implementado para los siguientes pares de números: (15,9); (9,15); (10,8); (12,6).

n=int(input("Introduce el segundo valor:"))
m=int(input("Introduce el primer valor:"))
mcd=0


while True:
    r=n%m
    if r==0:
        break
    else:
        n=m
        m=r
print("El mcd es", m)
