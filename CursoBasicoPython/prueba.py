
import time


objetivo=int(input("Escoje un enterno: "))
tiempo_inicial=time.time()
respuesta=0
while respuesta**2<objetivo:
    print(respuesta)
    respuesta+=1

if respuesta==object:
    print(f"La raíz cuadrada de {object} es {respuesta}")
else:
    print(f"{objetivo} no tiene raíz cuadrada exacta")

print(f'El programa demoró {time.time() - tiempo_inicial} segundos ')