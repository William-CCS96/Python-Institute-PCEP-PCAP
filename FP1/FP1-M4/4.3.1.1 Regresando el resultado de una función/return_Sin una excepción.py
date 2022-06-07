#RETURN SIN UNA EXCEPCIÓN

# La primera consiste en la palabra reservada en sí, sin nada que la siga.

# Cuando se emplea dentro de una función, provoca la terminación inmediata de la ejecución de la función, y un retorno instantáneo (de ahí el nombre) al punto de invocación.

# Nota: si una función no está destinada a producir un resultado, emplear la instrucción returnno es obligatorio, se ejecutará implícitamente al final de la función.

# De cualquier manera, se puede emplear para terminar las actividades de una función, antes de que el control llegue a la última línea de la función.


def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    print("¡Feliz año nuevo!")
happy_new_year()
# Tres...
# Dos...
# Uno...
# ¡Feliz año nuevo!

# Se modificará el comportamiento de la función; la instrucción return provocará su terminación justo antes de los deseos. Esta es la salida actualizada:
def happy_new_year(wishes = False):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    print("¡Feliz año nuevo!")
happy_new_year()
# Tres...
# Dos...
# Uno...

