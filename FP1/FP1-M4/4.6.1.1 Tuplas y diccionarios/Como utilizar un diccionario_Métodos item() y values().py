# ¿Cómo utilizar un diccionario? Los métodos item() y values()

#----------------------
# ITEM()
# Otra manera de hacerlo es utilizar el método items(). Este método regresa una lista de tuplas (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.

# Así es como funciona:
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)

# Nota la manera en que la tupla ha sido utilizada como una variable del bucle for.
# El ejemplo imprime lo siguiente:

    # gato -> chat
    # perro -> chien
    # caballo -> cheval


#----------------------
# VALUES()  
# También existe un método denominado values(), funciona de manera muy similar al de keys(), pero regresa una lista de valores.
# Este es un ejemplo sencillo:
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dictionary.values():
    print(french)

# Como el diccionario no es capaz de automáticamente encontrar la clave de un valor dado, el rol de este método es algo limitado.
# Esta es la salida esperada:

    # chat
    # chien
    # cheval

dd={"1": "0", "0": "1"}
for x in dd.values():
    print(x, end="")