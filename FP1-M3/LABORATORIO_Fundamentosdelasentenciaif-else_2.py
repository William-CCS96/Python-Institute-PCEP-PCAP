#Escenario
    # Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.
    # 
    # Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

# Si el número del año no es divisible entre cuatro, es un año común.
# De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# De lo contrario, si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.
# Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

#El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.

##Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.


from msilib import type_binary
from tkinter.messagebox import YESNOCANCEL


year = int(input("Introduce un año:"))
typeYear="Year"
if year<1582:
    typeYear="No incluido dentro del período del calendario Gregoriano"
elif year%4!=0:
    typeYear="Año común"
elif year%100!=0:
    typeYear="Año Bisiesto"
elif year%400!=0:
    typeYear="Año común"
else:
    typeYear="Año Bisiesto"
print(typeYear)
    #2000 
        #  Año Bisiesto
    #2015
        #  Año común 
    #1999
        #  Año común
    #1996
        #  Año Bisiesto
    #1580
        #  No incluido dentro del período del calendario Gregoriano
x = 1
y = 1.0
z = "1"

print(y==x)
print(y==int(z))



