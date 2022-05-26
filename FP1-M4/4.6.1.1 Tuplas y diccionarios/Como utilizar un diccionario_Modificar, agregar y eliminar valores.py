# ¿Cómo utilizar un diccionario? Modificar, agregar y eliminar valores
# El asignar un nuevo valor a una clave existente es sencillo, debido a que los diccionarios son completamente mutables, no existen obstáculos para modificarlos.

# Se va a reemplazar el valor "chat" por "minou", lo cual no es muy adecuado, pero funcionará con nuestro ejemplo.

# Observa:
dictionary = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)
    # {'gato': 'minou', 'dog': 'chien', 'caballo': 'cheval'}
dictionary["dog"] = 'perrito'
print(dictionary)
    # {'gato': 'minou', 'dog': 'perrito', 'caballo': 'cheval'}

# ------------------------------
# Agregando nuevas claves
# El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor. Solo se tiene que asignar un valor a una nueva clave que no haya existido antes.

# Nota: este es un comportamiento muy diferente comparado a las listas, las cuales no permiten asignar valores a índices no existentes.

# A continuación se agrega un par nuevo al diccionario, un poco extraño pero válido:
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)
    # {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'cisne': 'cygne'}

#-----------------------------
# También es posible insertar un elemento al diccionario utilizando el método update(), por ejemplo:

dictionary.update({"pato": "canard"})
print(dictionary)
    # {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'cisne': 'cygne', 'pato': 'canard'}

# ----------------------------
# Eliminado una clave
# ¿Puedes deducir como eliminar una clave de un diccionario?

# Nota: al eliminar la clave también se removerá el valor asociado. Los valores no pueden existir sin sus claves.

# Esto se logra con la instrucción del.

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dictionary['perro']
print(dictionary)
    # {'gato': 'chat', 'caballo': 'cheval'}
# Nota: el eliminar una clave no existente, provocará un error.

# --------------------------
# Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem():

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dictionary.popitem()
print(dictionary)   
# salida: {'gato': 'chat', 'perro': 'chien'}

# En versiones anteriores de Python, por ejemplo, antes de la 3.6.7, el método popitem() elimina un elemento al azar del diccionario.

