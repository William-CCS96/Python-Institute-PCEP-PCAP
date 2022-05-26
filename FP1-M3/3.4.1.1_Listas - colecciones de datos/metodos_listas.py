# AGREGAR ELEMENTOS A UNA LISTA    append() e insert()

    #Un nuevo elemento puede ser añadido al final de la lista existente:
#list.append(value)

    #El método insert() es un poco más inteligente: puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.
#list.insert(location, value)

numbers=[3,4,1,6]
print(len(numbers))

numbers.append(9)
print(numbers)
    #[3, 4, 1, 6, 9]
print(len(numbers))

numbers.insert(3,5)
print(numbers)
    #[3, 4, 1, 5, 6, 9]
print(len(numbers))

#CREAR LISTA VACIA
my_list=[]

for i in range(5):
     my_list.append(i+1)
print(my_list)
    #[1, 2, 3, 4, 5]

    #metodo inverso con insert()
for i in range(5):
    my_list.insert(0,i+1)
print(my_list)
    #[5, 4, 3, 2, 1]

