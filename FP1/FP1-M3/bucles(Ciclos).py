#while 
   #Bucle sin fin
    #while True:
        #print("Estoy atrapado dentro de un bucle.")
            #Para terminar el ciclo ctrl+c // KeyboardInterrupt

# Almacena el actual número más grande aquí.


#Hallar el número más grande entre un conjunto de números
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number)

#MAS EJEMPLOS
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:  # Tambien es posible así: while number != 0: y while number:
    # Verificar si el número es impar.
    if number % 2 == 1:    # Tambien es posible así:  if number % 2 == 1: y if number % 2:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)



#  SALIR DEL BUCLE CON counter

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
    # Dentro del bucle. 4
    # Dentro del bucle. 3
    # Dentro del bucle. 2
    # Dentro del bucle. 1
    # Fuera del bucle. 0

    #DE FORMAS MÁS COMPACTA 
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

        #RECUERDA
             # No te sientas obligado a codificar tus programas de una manera que siempre sea la más corta y la más compacta. La legibilidad puede ser un factor más importante. Manten tu código listo para un nuevo programador.



