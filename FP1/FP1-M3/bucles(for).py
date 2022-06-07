#Ejecutar el ciclo while 100 veces exactamente
i = 11

while i < 100:
    # do_something()
    i += 1
print(i)

#CICLO FOR
    #for i in range(100):
    # do_something()
    #pass


for i in range(10):
    print("El valor de i es actualmente", i)
    # El valor de i es actualmente 0
    # El valor de i es actualmente 1
    # El valor de i es actualmente 2
    # El valor de i es actualmente 3
    # El valor de i es actualmente 4
    # El valor de i es actualmente 5
    # El valor de i es actualmente 6
    # El valor de i es actualmente 7
    # El valor de i es actualmente 8
    # El valor de i es actualmente 9

    #El bucle se ha ejecutado diez veces (es el argumento de la función range()).
    # El valor de la última variable de control es 9 (no 10, ya que comienza desde 0 , no desde 1).

for i in range(2, 8):
    print("El valor de i es actualmente", i)
    # El valor de i es actualmente 2
    # El valor de i es actualmente 3
    # El valor de i es actualmente 4
    # El valor de i es actualmente 5
    # El valor de i es actualmente 6
    # El valor de i es actualmente 7

#Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.


#LA FUNCIÓN range() CON TRES ARGUMENTOS
    #El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada giro del bucle (como puedes sospechar, el valor predeterminado del incremento es 1).
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)
    # El valor de i es actualmente 2
    # El valor de i es actualmente 5

for i in range(1, 1): #Nota: si el conjunto generado por la función range() está vacío, el bucle no ejecutará su cuerpo en absoluto.Al igual que aquí, no habrá salida:
    print("El valor de i es actualmente", i)

#NOTA:  Los argumentos deben ordenarse de forma ascendente,el primer argumento debe ser mayor que el primero

#Programa para escribir las primeraspotencias de 2
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power) #Primero se ejecuta power =1 y despues se modifica su valor en la siguiente linea de código
    power *= 2
    # 2 a la potencia de 0 es 1
    # 2 a la potencia de 1 es 2
    # 2 a la potencia de 2 es 4
    # 2 a la potencia de 3 es 8
    # 2 a la potencia de 4 es 16
    # 2 a la potencia de 5 es 32
    # 2 a la potencia de 6 es 64
    # 2 a la potencia de 7 es 128
    # 2 a la potencia de 8 es 256
    # 2 a la potencia de 9 es 512
    # 2 a la potencia de 10 es 1024
    # 2 a la potencia de 11 es 2048
    # 2 a la potencia de 12 es 4096
    # 2 a la potencia de 13 es 8192
    # 2 a la potencia de 14 es 16384
    # 2 a la potencia de 15 es 32768
    # 2 a la potencia de 14 es 32768
    # 2 a la potencia de 15 es 65536


