from math import dist
from turtle import st


dist_a=int(float(input("Introduce la dimensión a:")))
dist_b=int(float(input("Introduce la dimensión b:")))

print("La suma entre la distancia "+str(dist_a)+" y "+str(dist_b)+" es igual a "+str(dist_a+dist_b))
print("La resta entre la distancia "+str(dist_a)+" y "+str(dist_b)+" es igual a "+str(dist_a-dist_b))
print("La multiplicación entre la distancia "+str(dist_a)+" y "+str(dist_b)+" es igual a "+str(dist_a*dist_b))
print("La división entre la distancia "+str(dist_a)+" y "+str(dist_b)+" es igual a "+str(dist_a/dist_b))
print("La división entera entre la distancia "+str(dist_a)+" y "+str(dist_b)+" es igual a "+str(dist_a//dist_b))
print("El módulo entre la distancia "+str(dist_a)+" y "+str(dist_b)+" es igual a "+str(dist_a%dist_b))
print("\n¡Eso es todo amigos!")