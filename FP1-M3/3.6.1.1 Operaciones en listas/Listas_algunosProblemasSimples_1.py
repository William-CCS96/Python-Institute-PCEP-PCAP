# El primero de ellos intenta encontrar el valor mayor en la lista. Mira el código en el editor.

my_list=[15,58,47,89,586,42,35,67]
largest=my_list[0]

for i in my_list:
    if i>largest:
        largest=i
print(largest)
    # 586

#El programa anterior realiza una comparación innecesaria, cuando el primer elemento se compara consigo mismo, pero esto no es un problema en absoluto.

# Si necesitas ahorrar energía de la computadora, puedes usar una rebanada:
my_list = [3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


#Como funciona el código:
my_list = [3, 11, 5, 1, 9, 7, 48, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


