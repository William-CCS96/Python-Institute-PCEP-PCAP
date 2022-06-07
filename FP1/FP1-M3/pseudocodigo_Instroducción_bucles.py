
#Function max()

# Se leen tres números.
from subprocess import HIGH_PRIORITY_CLASS


number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number
    
largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)



#Function max()
# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))





# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number
    
largest_number = min(number1, number2, number3)

# Imprime el resultado.
print("El número más pequeño es:", largest_number)



#LABORATORIO

florDeLaPaz = input("¿Cuál es la planta de cuna de Moisés?")

if florDeLaPaz=="ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
elif florDeLaPaz=="espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No "+florDeLaPaz+"!")

