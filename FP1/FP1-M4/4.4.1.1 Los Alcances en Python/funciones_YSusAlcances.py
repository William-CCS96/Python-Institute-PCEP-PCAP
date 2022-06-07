# El alcance de un nombre (por ejemplo, el nombre de una variable) es la parte del código donde el nombre es reconocido correctamente.

# Por ejemplo, el alcance del parámetro de una función es la función en sí. El parámetro es inaccesible fuera de la función.

# def scope_test():
#     x = 123


# scope_test()
# print(x)
    # NameError: name 'x' is not defined

#UNA VARIABLES CREADA POR FUERA DE UNA FUNCIÓN ES VISIBLE DENTRO DE UNA FUNCIÓN:
def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)
    # ¿Conozco a la variable? 1
    # 1

    #ESTA REGLA TIENE UNA EXCEPCIÓN
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)
    # ¿Conozco a la variable? 2
    # 1
            # La variable var creada dentro de la función no es la misma que la que se definió fuera de ella, parece ser que hay dos variables diferentes con el mismo nombre.
            # La variable de la función es una sombra de la variable fuera de la función.

"""Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre."""

#------------------------------
    #PALABRA CLAVE RESERVADA:  global

        # Al llegar a este punto, debemos hacernos la siguiente pregunta: ¿Una función es capaz de modificar una variable que fue definida fuera de ella? Esto sería muy incomodo.
            # Afortunadamente, la respuesta es no.

        # Existe un método especial en Python el cual puede extender el alcance de una variable incluyendo el cuerpo de las funciones para poder no solo leer los valores de las variables sino también modificarlos.
            # Este efecto es causado por la palabra clave reservada llamada global:

            # global name
            # global name1, name2, ...

        # El utilizar la palabra reservada dentro de una función con el nombre o nombres de las variables separados por comas, obliga a Python a abstenerse de crear una nueva variable dentro de la función; se empleará la que se puede acceder desde el exterior.

        # En otras palabras, este nombre se convierte en global (tiene un alcance global, y no importa si se esta leyendo o asignando un valor).

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 5
my_function()
print(var)
    # ¿Conozco a aquella variable? 2
    # 2
