# se deben colocar primero los argumentos posicionales y después los de palabra clave.

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(1,2,3)
    # 1 + 2 + 3 = 6
adding(c = 1, a = 2, b = 3)
    # 2 + 3 + 1 = 6

#COMBINANDO POSICIONALES Y PALABRA CLAVE:
adding(3, c = 1, b = 2)
    # 3 + 2 + 1 = 6

#ERROOORR
adding(3, a = 1, b = 2) #se le esta asignando dos veces un valor al parámetro a
