
# El ordenamiento burbuja - versión interactiva
# En el editor, puedes ver un programa completo, enriquecido por una conversación con el usuario, y que permite ingresar e imprimir elementos de la lista: El ordenamiento burbuja: versión final interactiva.

my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

# Python, sin embargo, tiene sus propios mecanismos de clasificación. Nadie necesita escribir sus propias clases, ya que hay un número suficiente de herramientas listas para usar.
# Si quieres que Python ordene tu lista, puedes hacerlo de la siguiente manera:

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
    # [2, 4, 6, 8, 10]

# 2.También hay un método de lista llamado reverse(), que puedes usar para invertir la lista, por ejemplo:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # salida: [4, 2, 1, 3, 5]

# Ejercicio 1
# ¿Cuál es la salida del siguiente fragmento de código?

lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)
    #['A', 'D', 'F', 'Z']

# Ejercicio 2
# ¿Cuál es la salida del siguiente fragmento de código?

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)
    # [1, 2, 3]

# Ejercicio 3
# ¿Cuál es la salida del siguiente fragmento de código?

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)
    #[' ', 'C', 'B', 'A']

