#Imprimir números impares

from doctest import REPORTING_FLAGS


for i in range(1, 11):
    if i%2==1:
        print(i)
  
#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.

x = 0
while x < 11:
    if x%2!=0:
        print(x)
    x+=1

#Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
print()

#Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue 
    print(digit, end="")

        # Línea de código.
        # Línea de código.
    # Línea de código.

a=5
print(a)



print()
#SALIDA DELSIGUIENTE CÓDIGO:}

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

#4
#3
#2
#0


#SALIDA DELSIGUIENTE CÓDIGO:

n = range(4)

for num in n:
    print(num - 1)
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

#-1
#0
#1
#2
#3 #num

#SALIDA DELSIGUIENTE CÓDIGO:
for i in range(0, 6, 3):
    print(i)

#0
#3


