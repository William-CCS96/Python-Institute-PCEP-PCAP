
numbers=[15,48,25,68,58]

print(numbers[0]) # Accediendo al primer elemento de la lista.
    # 15
print(numbers)  # Imprimiendo la lista completa
    # [15, 48, 25, 68, 58]

# FUNCIÓN len()
    #Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).

print("\nLa longitud de la lista numbers es: ", len(numbers))
    #La longitud de la lista numbers es:  5

#ELIMINANDO ELEMENTOS del()
    # Es una instrucción no una función
del(numbers[3])
print(len(numbers))
print(numbers)
    # 4
    # [15, 48, 25, 58]

#INDICES NEGATICOS SON VALIDOS
    #Un elemento con un índice igual a -1 es el último en la lista.
print(numbers[-1])
    # 58
print(numbers[-2])
    # 25
print(numbers[-4])
    # 15