
# Objetivos
# Perfeccionar las habilidades del estudiante al emplear Python para resolver problemas complejos.
# La integración de técnicas de programación en un solo programa consistente de varias partes.
"""# Escenario"""
# Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

    # La maquina (por ejemplo, el programa) jugará utiliz,o las 'X's.
    # El usuario (por ejemplo, tu) jugarás utiliz,o las 'O's.
    # El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
    # Todos los cuadros están numerados comenz,o con el 1 (observa el ejemplo para que tengas una referencia).
    # El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
    # El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
    # La maquina responde con su movimiento y se verifica el estado del juego.
    # No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

# El ejemplo del programa es el siguiente:
"""
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
¡Has Ganado!"""

# Requerimientos
# Implementa las siguientes características:

# El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

"""board[row][column]"""


# Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito represent,o el número del cuadro (dicho cuadro se considera como libre).
# La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
# Implementa las funciones definidas para ti en el editor.

# Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada r,range(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

# Nota: La instrucción from-import provee acceso a la función r,range definida en un módulo externo de Python denominado r,om.
"""
from r,om import r,range

for i in range(10):
    print(r,range(8))"""

#ESTRUCTURA

"""def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero."""




import random
import time

menu_inicio=(
    """
JUEGO TIC-TAC-TOE 🚀
Las computadora ya hizo su movimeinto (X), cual es tu movimiento (O)
    """
)
print(menu_inicio)

position=[0,1,2,3,4,"X",6,7,8,9]

def DisplayBoard():
    board=("+-------+-------+-------+"+\
    "\n|       |       |       |"+\
    "\n|   "+str(position[1])+"   |   "+str(position[2])+"   |   "+str(position[3])+"   |"+\
    "\n|       |       |       |"+\
    "\n|   "+str(position[4])+"   |   "+str(position[5])+"   |   "+str(position[6])+"   |"+\
    "\n|       |       |       |"+\
    "\n|   "+str(position[7])+"   |   "+str(position[8])+"   |   "+str(position[9])+"   |"+\
    "\n|       |       |       |"+\
    "\n+-------+-------+-------+")
    print(board)
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
        
def EnterMove():
    while True:
        try:
            movement=int(input("Ingresa tu movimiento: "))
            if movement in range(1,10):
                if position[movement]=="X" or position[movement]=="O":
                    print("la posición",movement,"ya está ocupada por una",position[movement])
                    continue
                break
            else:
                print("Valor incorrecto, indica una posición entre 1 y 9")
        except:
            print("Valor incorrecto, indica un número entre 1 y 9")
    position[movement]="O"
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.


# def MakeListOfFreeFields(board):

    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
def empate_fun():
    for i in position[1:10]:
        if i=="X" or i=="O":
            empate="Si"
            continue
        else: 
            empate="No"
            break
    return empate

def VictoryFor():
    if (position[1]=="X" and position[2]=="X" and position[3]=="X") or\
       (position[4]=="X" and position[5]=="X" and position[6]=="X") or\
       (position[7]=="X" and position[8]=="X" and position[9]=="X") or\
       (position[1]=="X" and position[4]=="X" and position[7]=="X") or\
       (position[2]=="X" and position[5]=="X" and position[8]=="X") or\
       (position[3]=="X" and position[6]=="X" and position[9]=="X") or\
       (position[1]=="X" and position[5]=="X" and position[9]=="X") or\
       (position[7]=="X" and position[5]=="X" and position[3]=="X"):
       return "Computer"
    elif (position[1]=="O" and position[2]=="O" and position[3]=="O") or\
       (position[4]=="O" and position[5]=="O" and position[6]=="O") or\
       (position[7]=="O" and position[8]=="O" and position[9]=="O") or\
       (position[1]=="O" and position[4]=="O" and position[7]=="O") or\
       (position[2]=="O" and position[5]=="O" and position[8]=="O") or\
       (position[3]=="O" and position[6]=="O" and position[9]=="O") or\
       (position[1]=="O" and position[5]=="O" and position[9]=="O") or\
       (position[7]=="O" and position[5]=="O" and position[3]=="O"):
       return "User"  
    elif empate_fun()=="Si":
        return "Empate"
    else:
        return "Continue"
    
        # La función analiza el estatus del tablero para verificar si
        # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

def DrawMove():
    while True:
        x=int(random.randint(1,9))
        if position[x]=="X"or position[x]=="O":
            continue
        else:
            position[x]="X"
            break
     # La función dibuja el movimiento de la máquina y actualiza el tablero.

def game_again():
    while True:
        again=int(input("¿Deseas jugar de nuevo?, 1.Si ó 2.No "))
        if again==1:
            return "Continue"
        if again==2:
            print("¡Gracias!")
            return "Finish"
        else:
            print("Valor incorrecto, indica 1 ó 2 ")


#Game:
while True:
    DisplayBoard()
    EnterMove()
    if VictoryFor()=="User":
        DisplayBoard()
        print("¡Felicitaciones, has ganado!")
        if game_again()=="Continue":
            position=[0,1,2,3,4,"X",6,7,8,9]
            continue
        else:
            time.sleep(3)
            break
    DisplayBoard()
    print("Turno para la computadora, espera un momento")
    time.sleep(2.5)
    DrawMove()
    if VictoryFor()=="Computer":
        DisplayBoard()
        print("¡Gana la computadora")
        if game_again()=="Continue":
            position=[0,1,2,3,4,"X",6,7,8,9]
            continue
        else:
            time.sleep(3)
            break
    elif VictoryFor()=="Continue":
        continue
    elif VictoryFor()=="Empate":
        DisplayBoard()
        print("Has empatado con la computadora")
        if game_again()=="Continue":
            position=[0,1,2,3,4,"X",6,7,8,9]
            continue
        else:
            time.sleep(3)
            break
    

        








