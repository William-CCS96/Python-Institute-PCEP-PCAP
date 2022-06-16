"""Puntos Claves"""

# 1. Las cadenas son herramientas clave en el procesamiento de datos modernos, ya que la mayoría de los datos útiles son en realidad cadenas. Por ejemplo, el uso de un motor de búsqueda web (que parece bastante trivial en estos días) utiliza un procesamiento de cadenas extremadamente complejo, que involucra cantidades inimaginables de datos.

# 2. El comparar cadenas de forma estricta (como lo hace Python) puede ser muy insatisfactorio cuando se trata de búsquedas avanzadas (por ejemplo, durante consultas extensas a bases de datos). En respuesta a esta demanda, se han creado e implementado una serie de algoritmos de comparación de cadenas difusos. Estos algoritmos pueden encontrar cadenas que no son iguales en el sentido de Python, pero que son similares.

# Uno de esos conceptos es la Distancia Hamming, que se utiliza para determinar la similitud de dos cadenas. Si este tema te interesa, puedes encontrar más información al respecto aquí: https://en.wikipedia.org/wiki/Hamming_distance. Otra solución del mismo tipo, pero basada en un supuesto diferente, es la Distancia Levenshtein descrita aquí: https://en.wikipedia.org/wiki/Levenshtein_distance.


# 3. Otra forma de comparar cadenas es encontrar su similitud acústica, lo que significa un proceso que lleva a determinar si dos cadenas suenan similares (como "echo" y "hecho"). Esa similitud debe establecerse para cada idioma (o incluso dialecto) por separado.

# Un algoritmo utilizado para realizar una comparación de este tipo para el idioma Inglés se llama Soundex y se inventó, no lo creerás, en 1918. Puedes encontrar más información al respecto aquí: https://en.wikipedia.org/wiki/Soundex.


# 4. Debido a la precisión limitada de los datos enteros y flotantes nativos, a veces es razonable almacenar y procesar valores numéricos enormes como cadenas. Esta es la técnica que usa Python cuando se le fuerza a operar con un número entero que consta de una gran cantidad de dígitos.


def  hamming_distance ( cadena1 ,  cadena2 ): 
	dist_counter  =  0 
	for  n  in  range ( len ( cadena1 )): 
		if  cadena1 [ n ]  !=  cadena2 [ n ]: 
			dist_counter  +=  1 
	return  dist_counter

print(hamming_distance("ete","iti"))

