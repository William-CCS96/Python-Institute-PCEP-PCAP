"""La pila: el enfoque procedimental"""
# Primero, debes decidir como almacenar los valores que llegarán a la pila. Sugerimos utilizar el método más simple, y emplear una lista para esta tarea. Supongamos que el tamaño de la pila no está limitado de ninguna manera. Supongamos también que el último elemento de la lista almacena el elemento superior.

# La pila en sí ya está creada:

stack = []

# Estamos listos para definir una función que coloca un valor en la pila. Aquí están las presuposiciones para ello:

    # El nombre para la función es push.
    # La función obtiene un parámetro (este es el valor que se debe colocar en la pila).
    # La función no retorna nada.
    # La función agrega el valor del parámetro al final de la pila.
# Así es como lo hemos hecho, echa un vistazo:

def push(val):
    stack.append(val)

# Ahora es tiempo de que una función quite un valor de la pila. Así es como puedes hacerlo:

    # El nombre de la función es pop.
    # La función no obtiene ningún parámetro.
    # La función devuelve el valor tomado de la pila.
    # La función lee el valor de la parte superior de la pila y lo elimina.
# La función esta aqui:

def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Nota: la función no verifica si hay algún elemento en la pila.

# Armemos todas las piezas juntas para poner la pila en movimiento. El programa completo empuja (push) tres números a la pila, los saca e imprime sus valores en pantalla. Puedes verlo en la ventana del editor.

# El programa muestra el siguiente texto en pantalla:

# 1
# 2
# 3
# salida

# Pruébalo.

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
    # 1
    # 2
    # 3