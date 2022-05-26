# ¿De dónde provienen las funciones?
# En general, las funciones provienen de al menos tres lugares:

# De Python mismo: varias funciones (como print()) son una parte integral de Python, y siempre están disponibles sin algún esfuerzo adicional del programador; se les llama a estas funciones integradas.
       """ FUNCIONES INTEGRADAS :https://docs.python.org/3/library/functions.html"""
# De los módulos preinstalados de Python: muchas de las funciones, las cuales comúnmente son menos utilizadas que las integradas, están disponibles en módulos instalados juntamente con Python; para poder utilizar estas funciones el programador debe realizar algunos pasos adicionales (se explicará acerca de esto en un momento).
# Directamente del código: tu puedes escribir tus propias funciones, colocarlas dentro del código, y usarlas libremente.
# Existe una posibilidad más, pero se relaciona con clases, se omitirá por ahor

# print("Ingresa un valor: ")
# a = int(input())

# print("Ingresa un valor: ")
# b = int(input())

# print("Ingresa un valor: ")
# c = int(input())
#     #Con una función se puede dejar la invocación en unasola linea

# def function_name():
#     function_body

def message():
    print("Ingresa un valor: ")
print("Se comienza aquí.")
message()
print("Se termina aquí.")

    # No se debe invocar una función antes de que se haya definido.
    # Una función y una variable no pueden compartir el mismo nombre.
    #CÓDIGO ERRONEO:
def message():
    print("Ingresa un valor: ")

message = 1 #ERRRORRR

# -------------------------------
# Afortunadamente, es posible combinar o mezclar el código con las funciones - no es forzoso colocar todas las funciones al inicio del archivo fuente.
# Observa el siguiente código:

print("Se comienza aquí.")

def message():
    print("Ingresa un valor: ")

message()

print("Se termina aquí.")

# -------------------------------

# Regresemos al ejemplo inicial para implementar la función de manera correcta:

def message():
    print("Ingresa un valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

# ------------------------------
# También es posible definir funciones con argumentos, como la siguiente que contiene un solo parámetro:

def hello(name):    # definiendo una función
    print("Hola,", name)    # cuerpo de la función

name = input("Ingresa tu nombre: ")

hello(name)    # invocación de la función
