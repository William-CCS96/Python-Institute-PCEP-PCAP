

    # ¿Qué es un diccionario?
# El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.

# Para explicar lo que es un diccionario en Python, es importante comprender de manera literal lo que es un diccionario.

# Un diccionario en Python funciona de la misma manera que un diccionario bilingüe. Por ejemplo, se tiene la palabra en español "gato" y se necesita su equivalente en francés. Lo que se haría es buscar en el diccionario para encontrar la palabra "gato". Eventualmente la encontrarás, y sabrás que la palabra equivalente en francés es "chat".

# Concepto de Tuplas frente a Diccionarios

# En el mundo de Python, la palabra que se esta buscando se denomina 
clave(key)
# La palabra que se obtiene del diccionario es denominada
valor.

        # Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:

        # Cada clave debe de ser única. No es posible tener una clave duplicada.
        # Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante), o incluso una cadena.
        # Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores.
        # La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
        # Un diccionario es una herramienta de un solo sentido. Si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés más no viceversa.
# A continuación veamos algunos ejemplos:

# ¿Cómo crear un diccionario?
# Si deseas asignar algunos pares iniciales a un diccionario, utiliza la siguiente sintaxis:

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)


# En este primer ejemplo, el diccionario emplea claves y valores las cuales ambas son cadenas. En el segundo, las claves con cadenas pero los valores son enteros. El orden inverso (claves → números, valores → cadenas) también es posible, así como la combinación número a número.

# La lista de todos los pares es encerrada con llaves, mientras que los pares son separados por comas, y las claves y valores por dos puntos.

# El primer diccionario es muy simple, es un diccionario Español-Francés. El segundo es un directorio telefónico muy pequeño.

# Los diccionarios vacíos son construidos por un par vacío de llaves - nada inusual.


# El diccionario entero se puede imprimir con una invocación a la función print(). El fragmento de código puede producir la siguiente salida:

{'perro': 'chien', 'caballo': 'cheval', 'gato': 'chat'}
{'Suzy': 5557654321, 'jefe': 5551234567}
{}
salida


¿Has notado que el orden de los pares impresos es diferente a la asignación inicial?, ¿Qué significa esto?

Primeramente, recordemos que los diccionarios no son listas - no guardan el orden de sus datos, el orden no tiene significado (a diferencia de los diccionarios reales). El orden en que un diccionario almacena sus datos esta fuera de nuestro control. Esto es normal. (*)

NOTA

(*) En Python 3.6x los diccionarios se han convertido en colecciones ordenadas de manera predeterminada. Tu resultado puede variar dependiendo en la versión de Python que se este utilizando.

