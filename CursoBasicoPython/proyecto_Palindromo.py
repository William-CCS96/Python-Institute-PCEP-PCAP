# def palindromo():
#     if palabra==palabra[::-1]:
#         print("Es un palindromo ")
#     else:
#         print("No es palindromo")

# palabra=input("Escribe una palabra ")
# palindromo()

"""entry point/Punto de entrada"""

def palindromo(palabra):
    palabra=palabra.replace(" ", "")
    palabra=palabra.lower()
    palabra_inv=palabra[::-1]
    if palabra_inv==palabra:
        return True
    else: 
        return False    


def run():
    palabra=input("Escrbie una palabra")
    es_palindromo=palindromo(palabra)
    if es_palindromo==True:
        print("Es un palindromo ")
    else:
        print("No es palindromo ")


def run2():
    palabra = str(input("Escribe un palabra: ")).lower().replace(' ', '')
    if palabra== palabra[::-1]:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

#Elpunto de entrada del programa de entrada 
#Empieza a correr todo lo que hay debajo
#Despues de esta invocación el programa va a empezar a correr todo lo que hay debajo
if __name__ == "__main__":
    run()
    run2()


