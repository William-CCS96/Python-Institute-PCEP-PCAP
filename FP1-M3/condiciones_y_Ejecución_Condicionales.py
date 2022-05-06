#INTRUCCIONES CONDICIONALES // SENTENCIA CONDICIONAL

    #if true_or_not:
        # do_this_if_true

    #Todas las instrucciones deben estar separadas con la misma sangria

            #En la vida real, a menudo expresamos un deseo:
                # si el clima es bueno, saldremos a caminar
                # después, almorzaremos
             # Como puedes ver, almorzar no es una actividad condicional y no depende del clima.
            #if the_weather_is_good:
            #     go_for_a_walk()
            # have_lunch()


            #if sheep_counter >= 120: # #evalúa una expresión condicional
            #     sleep_and_dream() #se ejecuta si la expresión condicional es True

    # IF-ELSE
        #if true_or_false_condition:
        #     perform_if_condition_true
        # else:
        #     perform_if_condition_false

            #if the_weather_is_good:
            #     go_for_a_walk()
            # else:
            #     go_to_a_theater()
            # have_lunch()

            # if the_weather_is_good:
            #     go_for_a_walk()
            #     have_fun()
            # else:
            #     go_to_a_theater()
            #     enjoy_the_movie()
            # have_lunch()
    
#SENTENCIAS if-else ANIDADAS

            #if the_weather_is_good:
            #     if nice_restaurant_is_found:
            #         have_lunch()
            #     else:
            #         eat_a_sandwich()
            # else:
            #     if tickets_are_available:
            #         go_to_the_theater()
            #     else:
            #         go_shopping()

            #Cada else se refiere al if con el mismo nivel de sangria

#SENTENCIA ELIF //   Una forma más corta de else-if
        #Verificar más de una condición y para detener cuando se ecnuentre la primera sentencia verdadera
        #La forma de ensamblar las siguientes sentencias if-elif-else a veces se denomina cascada.


        #si hay buen clima, saldremos a caminar, de lo contrario, si obtenemos entradas, iremos al cine, de lo contrario, si hay mesas libres en el restaurante, vamos a almorzar; si todo falla, regresaremos a casa y jugaremos ajedrez. 

        #if the_weather_is_good:
        #     go_for_a_walk()
        # elif tickets_are_available:
        #     go_to_the_theater()
        # elif table_is_available:
        #     go_for_lunch()
        # else:
        #     play_chess_at_home()

#EJEMPLOS DE CODIGO
    #Todos los programas resuelven el mismo problema: encuentran el número mayor de una serie de números y lo imprimen.

    # Ejemplo 1   ¿Cómo identificar el mayor de los dos números?
number1=int(input("Ingresa tu primer número"))
number2=int(input("Ingresa tu segundo número"))

if number1>number2:
    larger_numer = number1
else:
    larger_numer = number2

print("El número más grande entre el", number1, "y el", number2, "es el:", larger_numer)
    # El número más grande entre el 58 y el 96 es el: 96

    # Ejemplo 2
    # Nota: si alguna de las ramas de if-elif-else contiene una sola instrucción, puedes codificarla de forma más completa (no es necesario que aparezca una línea con sangría después de la palabra clave), pero solo continúa la línea después de los dos puntos).
#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)


    # Ejemplo 3
number_1=int(input("Escribe tu primer número"))
number_2=int(input("Escribe tu segundo número"))
number_3=int(input("Escribe tu tercer número"))

larger_number_other=number_1

if number_2>larger_number_other:
    larger_number_other=number_2

if number_3>larger_number_other:
    larger_number_other>number_3

print("El número más grande es el: ", larger_number_other)








    
    