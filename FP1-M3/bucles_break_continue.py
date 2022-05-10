#Sin embargo, como desarrollador, podrías enfrentar las siguientes opciones:

#Parece que no es necesario continuar el bucle en su totalidad; se debe abstener de seguir ejecutando el cuerpo del bucle e ir más allá.
#Parece que necesitas comenzar el siguiente giro del bucle sin completar la ejecución del turno actual.

#Tales adiciones, que no mejoran el poder expresivo del lenguaje, sino que solo simplifican el trabajo del desarrollador, a veces se denominan dulces sintácticos o azúcar sintáctica.

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
    # La instrucción break:
    # Dentro del bucle. 1
    # Dentro del bucle. 2
    # Fuera del bucle.

# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
    # La instrucción continue:
    # Dentro del bucle. 1
    # Dentro del bucle. 2
    # Dentro del bucle. 4
    # Dentro del bucle. 5
    # Fuera del bucle.

#EJEMPLO break (NÚMERO MAYOR)
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

#EJEMPLO continue (NÚMERO MAYOR)

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
