# La primera es: ¿Se puede enviar una lista a una función como un argumento?

# ¡Por supuesto que se puede! Cualquier entidad reconocible por Python puede desempeñar el papel de un argumento de función, aunque debes asegurarte de que la función sea capaz de hacer uso de él.

# Entonces, si pasas una lista a una función, la función tiene que manejarla como una lista.

def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([1,2,3,4]))
    # 10

# Si se invoca así arroja ERRORRR:
    # print(list_sum(5))
    # Esto se debe al hecho de que el bucle for no puede iterar un solo valor entero.

#------------------------
# La segunda pregunta es: ¿Puede una lista ser el resultado de una función?

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
    # [4, 3, 2, 1, 0]
    
