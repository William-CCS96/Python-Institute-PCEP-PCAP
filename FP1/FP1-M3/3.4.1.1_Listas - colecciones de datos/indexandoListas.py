#Indexando listas
    # El valor dentro de los cochetes se denomina un indice
    # La operación de seleccionar un elemento de la lista se conoce como indexación.
    # Cualquier expresión también puede ser un índice
numbers=[10,5,4,3,2]
print("Contenido de la lista original: ", numbers)
    # Contenido de la lista original:  [10, 5, 4, 3, 2]

numbers[0]=111
print("\nNuevo contenido en la posición 0: ", numbers)
    # Nuevo contenido en la posición 0:  [111, 5, 4, 3, 2]

#Copiar elementos desde una posición a otra
numbers[1]=numbers[4]
print("\nValor copiado desde la posición 0 a la 4:", numbers)
    # Valor copiado desde la posición 0 a la 4: [111, 2, 4, 3, 2]


