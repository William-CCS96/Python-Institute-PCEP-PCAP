# Ejercicio 4.6.4. Escribir funciones que permitan encontrar:

# El máximo o minimo de un polinomio de segundo grado (dados los coeficientes a, b y c), indicando si es un máximo o un minimo.
# Las raíces (reales o complejas) de un polinomio de segundo grado. Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni calcular la raiz de un número negativo).
# La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta). Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.

import math

def max_min_PSG(a,b,c):
    if a==0:
        return print("El valor de (a) debe ser distinto a cero")
    if a>0:
        min=((4*a*c-(b**2))/(4*a))
        return print("El valor mínimo del polinomio de seguno grado es:",min)
    if a<0:
        max=((4*a*c-(b**2))/(4*a))
        return print("El valor maximo del polinomio de segundo grado es:",max)

max_min_PSG(-1,-2,3)
# El valor maximo del polinomio de segundo grado es: 4.0

def raices_PSG(a,b,c):
    discriminante=(b**2)-(4*a*c)
    if discriminante>=0:
        x1=(-(b)+math.sqrt(discriminante))/(2*a)
        x2=(-(b)-math.sqrt(discriminante))/(2*a)
        print("las soluciones en numeros reales del polinomio de segundo grado "+str(a)+"²"+"-"+str(b)+"x"+"+"+str(c)+" "+"son :", round(x1,2),"y",round(x2,2))
    if discriminante<0:
        print("El discriminante es menor que cero, por lo tanto la ecuación"+str(a)+"²"+"-"+str(b)+"x"+"+"+str(c)+" "+"no posee resulados con números reales")

raices_PSG(3,-5,1)
# las soluciones en numeros reales del polinomio de segundo grado 3²--5x+1 son : 1.43 y 0.23
raices_PSG(3,-1,7)
# El discriminante es menor que cero, por lo tanto la ecuación3²--1x+7 no posee resulados con números reales

def point_intersection(m1,b1,m2,b2):
    if m1==m2:
        return print("Las dos rectas son paralelas al tener pendientes iguales")
    x1=round(((b1-b2)/(m2-m1)),1)
    y1=round((((m2*b1)-(m1*b2))/(m2-m1)),1)
    print("la intersección de las dos rectas está en el punto: "+"("+str(x1)+","+str(y1)+")")

point_intersection(1,-1,(1/3),3)

# la intersección de las dos rectas está en el punto: (6.0,5.0)