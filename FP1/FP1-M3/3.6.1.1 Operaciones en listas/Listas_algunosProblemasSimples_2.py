# Ahora encontremos la ubicación de un elemento dado dentro de una lista:

list=[58,45,4,6,5,8,9,1]
to_find=58
found=False

for i in range(len(list)):
    found=list[i]==to_find
    if found:
        break
if found:
    print("El numero encuentrado dentro de la lista esta en la posición: ", i)
else:
    print("No se encontro el número dentro de la lista")

# Nota:
# El valor buscado se almacena en la variable to_find.
# El estado actual de la búsqueda se almacena en la variable found (True/False).
# Cuando found se convierte en True, se sale del bucle for.

#SEGUNDO PROGRAMA:
    # Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.
    # Los números que han salido sorteados son: 5, 11, 9, 42, 3, 49.
    # La pregunta es: ¿A cuántos números le has atinado?

drawn=[3,57,59,47,36,45,25]
lottery=[48,57,45,2,25,3]
success=0

for i in lottery:
    if i in drawn:
        success+=+1
print(success)
    # 4

    # Nota:
    # La lista drawn almacena todos los números sorteados.
    # La lista bets almacena los números con que se juega.
    # La variable hits cuenta tus aciertos.
    # La salida del programa es: 4.
