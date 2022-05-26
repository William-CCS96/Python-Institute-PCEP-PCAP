board = []
EMPTY=0

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print(board)
print(row)
    # [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    #Nota:

    # La parte interior del bucle crea una fila que consta de ocho elementos (cada uno de ellos es igual a EMPTY) y lo agrega a la lista del board.
    # La parte exterior se repite ocho veces.
    # En total, la lista board consta de 64 elementos (todos iguales a EMPTY).

# La variable board ahora es un arreglo bidimensional. También se le llama, por analogía a los términos algebraicos, una matriz.


    # Como las listas de comprensión puede ser anidadas, podemos acortar la creación del tablero de la siguiente manera:

board = [[EMPTY for i in range(8)] for j in range(8)]
    # La parte interna crea una fila, y la parte externa crea una lista de filas.

#------------------------------------

#El acceso al campo seleccionado del tablero requiere dos índices: el primero selecciona la fila; el segundo: el número del campo dentro de la fila, el cual es un número de columna.

# Echando un vistazo a la figura que se muestra arriba, coloquemos algunas piezas de ajedrez en el tablero. Primero, agreguemos todas las torres:
board[0][0] = ROOK #Rook/Torre
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

#Si deseas agregar un caballo a C4, hazlo de la siguiente manera:
board[4][2] = KNIGHT    #knight/caballero
#Y ahora un peón a E5:
board[3][4] = PAWN      #Pawn/peón


# Ejercicio:
EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)
    #[['TORRE', '-', '-', '-', '-', '-', '-', 'TORRE'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['TORRE', '-', '-', '-', '-', '-', '-', 'TORRE']]


