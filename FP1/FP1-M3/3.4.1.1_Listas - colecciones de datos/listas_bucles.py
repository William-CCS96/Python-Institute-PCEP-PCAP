#for
    #Supongamos que deseas calcular la suma de todos los valores almacenados en la lista my_list.

    # A la lista se le asigna una secuencia de cinco valores enteros.
    # La variable i toma los valores 0, 1,2,3, y 4, y luego indexa la lista, seleccionando los elementos siguientes: el primero, segundo, tercero, cuarto y quinto.
    # Cada uno de estos elementos se agrega junto con el operador += a la variable suma, dando el resultado final al final del bucle.
    # Observa la forma en que se ha empleado la función len(), hace que el código sea independiente de cualquier posible cambio en el contenido de la lista.

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
    # 27

#Segundo aspecto del bucle for
    
    # ¿Qué sucede aquí?

    # La instrucción for especifica la variable utilizada para navegar por la lista (i) seguida de la palabra clave in y el nombre de la lista siendo procesado (my_list).
    # A la variable i se le asignan los valores de todos los elementos de la lista subsiguiente, y el proceso ocurre tantas veces como hay elementos en la lista.
    # Esto significa que usa la variable i como una copia de los valores de los elementos, y no necesita emplear índices.
    # La función len() tampoco es necesaria aquí.

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)
    # 27

#LISTAS EN ACCIÓN
    #Revertir el orden de los elementos
variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary


    # Python ofrece una forma más conveniente de hacer el intercambio, echa un vistazo:

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

my_list=[5,4,3,2,1]
my_list[0],my_list[4]=my_list[4],my_list[0]
my_list[1],my_list[3]=my_list[3],my_list[1]
print(my_list)

#USAR BUCLE for PARA INVERTIR INDEPENDIENTEMENTE DE LA CANTIDAD

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
    #[5, 3, 8, 1, 10]

# Nota:
# Hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto).
# Hemos preparado el bucle for para que se ejecute su cuerpo length // 2 veces (esto funciona bien para listas con longitudes pares e impares, porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto).
# Hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length-i-1) (desde el final de la lista); en nuestro ejemplo, for i igual a 0 a la (length-i-1) da 4; for i igual a 3, da 3: esto es exactamente lo que necesitábamos.
