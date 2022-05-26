# ¿Cómo utilizar un diccionario?
# Si deseas obtener cualquiera de los valores, debes de proporcionar una clave válida:
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}
print(dictionary['gato'])
print(phone_numbers['Suzy'])

# El obtener el valor de un diccionario es semejante a la indexación, gracias a los corchetes alrededor del valor de la clave.

# Nota:
    # Si una clave es una cadena, se tiene que especificar como una cadena.
    # Las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.
    # El fragmento de código da las siguientes salidas:

        # chat
        # 5557654321
        # salida

# Ahora algo muy importante: No se puede utilizar una clave que no exista. Hacer algo como lo siguiente:
# print(phone_numbers['presidente'])
# Provocará un error de ejecución. Inténtalo.

# Afortunadamente, existe una manera simple de evitar dicha situación. El operador in, junto con su acompañante, not in, pueden salvarnos de esta situación.
# El siguiente código busca de manera segura palabras en francés:

diccionary={"mico":"salta", "gato":"trepa", "serpiente":"repta"}
animals=["caballo", "pato", "serpiente"]
phone_number={"William":3166202421,"Juanito":3152566578}

for word in animals:
    if word in diccionary:
        print(word,"=>", diccionary[word])
    else:
        print(word, "no está en el diccionario(diccionary).")
        # caballo no está en el diccionario(diccionary).
        # pato no está en el diccionario(diccionary).
        # serpiente => repta

# Cuando escribes una expresión grande o larga, puede ser una buena idea mantenerla alineada verticalmente. Así es como puede hacer que el código sea más legible y más amigable para el programador, por ejemplo:

# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
              }

# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
                 'Suzy': 22657854310
                 }


            # Este tipo de formato se llama sangría francesa.

            