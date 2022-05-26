# Escenario
# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.

# Tu tarea es:

# Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1).
# Escribir una línea de código que elimine el último elemento de la lista (Paso 2).
# Escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
# ¿Listo para este desafío?

hat_list=[1,2,3,4,5]

hat_list[2]=int(input("Ingresa el número que deseas reemplazar: "))
del(hat_list[-1])
print(hat_list)
print("\nLa longitud de la lista hat_list es: ", len(hat_list))
