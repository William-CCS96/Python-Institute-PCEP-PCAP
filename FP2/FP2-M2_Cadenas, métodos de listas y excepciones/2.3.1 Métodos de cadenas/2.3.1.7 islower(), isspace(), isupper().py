"""El método islower()"""
# El método islower() es una variante de isalpha() - solo acepta letras minúsculas.

# Ejemplo 1: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())
print("dfjfK89".islower())
    # False
    # True


"""El método isspace()"""
# El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro carácter (el resultado es entonces False).

# Ejemplo 2: Demostración del método isspace(:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
    # True
    # True
    # False

"""El método isupper()"""
# El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.

# Ejemplo 3: Demostración del método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
print("1".islower())
    # False
    # False
    # True