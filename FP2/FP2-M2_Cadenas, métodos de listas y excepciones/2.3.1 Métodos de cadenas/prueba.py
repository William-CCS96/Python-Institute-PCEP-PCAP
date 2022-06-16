print("\"Un divertido "+"programa "+"de radio.\"")
print("Hola, "+"hola, "*4+"tú")
a="Hola mundo mundano"
print(len(a))
b=""
print(len(b))
for letter in a:
    print(letter,end=" ")
print()
print(a[-1])
# Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres de una cadena del final al principio.
for letter in range(len(a)):
    print(a[(letter+1)*-1],end="")

print()

cadena=""
cadena+="sd.45"
print(cadena)
print(len(cadena))

print(cadena[0])