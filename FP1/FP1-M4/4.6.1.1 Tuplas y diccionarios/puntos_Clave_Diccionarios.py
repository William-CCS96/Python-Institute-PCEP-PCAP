# Puntos Clave: Diccionarios

# 1. Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. (*En Python 3.6x los diccionarios están ordenados de manera predeterminada.

# Cada diccionario es un par de clave : valor. Se puede crear empleado la siguiente sintaxis:
from traceback import print_tb


my_dictionary={
    "Cosmos":"Carl Sagan",
    "Religión":"Estiocismo",
    "Habito":"Agradecimiento",
}
print(my_dictionary)

# 2. Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola dentro de corchetes (Ejemplo 1) o utilizando el método get() (Ejemplo 2):

option_1=my_dictionary["Cosmos"]
print(option_1)  # Carl Sagan
option_2=my_dictionary.get("Habito")
print(option_2) # Agradecimiento

# 3. Si se desea cambiar el valor asociado a una clave específica, se puede hacer haciendo referencia a la clave del elemento, a continuación se muestra un ejemplo:
my_dictionary["Cosmos"]="Yuval Harari"
option_3=my_dictionary["Cosmos"]
print(option_3)  # Yuval Harari

# 4. Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:

my_dictionary["Tiempo"]="Efimero"
print(my_dictionary)
    # {'Cosmos': 'Yuval Harari', 'Religión': 'Estiocismo', 'Habito': 'Agradecimiento', 'Tiempo': 'Efimero'}

del my_dictionary["Tiempo"]
print(my_dictionary)
    # {'Cosmos': 'Yuval Harari', 'Religión': 'Estiocismo', 'Habito': 'Agradecimiento'}

# Además, se puede insertar un elemento a un diccionario utilizando el método update(), y eliminar el ultimo elemento con el método popitem(), por ejemplo:

my_dictionary.update({"Tiempo":"Efimero"})
print(my_dictionary)
    # {'Cosmos': 'Yuval Harari', 'Religión': 'Estiocismo', 'Habito': 'Agradecimiento', 'Tiempo': 'Efimero'}
my_dictionary.popitem()
print(my_dictionary)
    # {'Cosmos': 'Yuval Harari', 'Religión': 'Estiocismo', 'Habito': 'Agradecimiento'}

# 5. Se puede emplear el bucle for para iterar a través del diccionario, por ejemplo:

for i in my_dictionary:
    print(i)
    # Cosmos
    # Religión
    # Habito

# 6. Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items(), por ejemplo:
for key, value in my_dictionary.items():
    print("General/meaning", "->", key,":", value)  
        # General/meaning -> Cosmos : Yuval Harari
        # General/meaning -> Religión : Estiocismo
        # General/meaning -> Habito : Agradecimiento

# 7. Para comprobar si una clave existe en un diccionario, se puede emplear la palabra clave reservada in:

if "Cosmos" in my_dictionary:
    print("Si")
else:
    print("No")
    # Si

# 9. Para copiar un diccionario, emplea el método copy():

copy_my_dictionary=my_dictionary.copy()
print(copy_my_dictionary)
    # {'Cosmos': 'Yuval Harari', 'Religión': 'Estiocismo', 'Habito': 'Agradecimiento'}

# 8. Se puede emplear la palabra reservada del para eliminar un elemento, o un diccionario entero. Para eliminar todos los elementos de un diccionario se debe emplear el método clear():

print(len(my_dictionary))  # 2
del my_dictionary["Cosmos"]
print(len(my_dictionary))  # 3

my_dictionary.clear()
print(len(my_dictionary))  # 0
del my_dictionary
print(my_dictionary)    #NameError: name 'my_dictionary' is not defined



