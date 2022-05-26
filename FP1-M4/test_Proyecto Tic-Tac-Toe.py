import random

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

#Game:



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


while True:
    DisplayBoard()
    EnterMove()
    DrawMove()
    if VictoryFor()=="Computer":
        DisplayBoard()
        print("¡Gana la computadora")
    elif VictoryFor()=="User":
        DisplayBoard()
        print("¡Felicitaciones, has ganado!")
    elif VictoryFor()=="Continue":
        continue
    elif VictoryFor()=="Empate":
        DisplayBoard()
        print("Has empatado con la computadora")
    if game_again()=="Continue":
        position=[0,1,2,3,4,"X",6,7,8,9]
        continue
    else:
        break
