# Ejercicio 5.7.3. Manejo de contraseñas

# Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# Modificar el programa anterior para que solamente permita una cantidad fija de inten-tos.
# Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.
# Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

import time

password="Juanito"
count=1
second=5.0
while True:
    option_password=input("Digita tu contraseña: ")
    if password==option_password:
        print(True)
        break
    elif password!=option_password and count<3:
        count+=1
        print(False)
        time.sleep(second)
        second*=2
    elif count>=3:
        print(False)
        print("Has sobrepasado el número de intentos, espera 30 segundos para volver a intentar")
        time.sleep(60)
        count=1
        second=5.0


