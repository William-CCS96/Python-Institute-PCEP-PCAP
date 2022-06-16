"""El método isalpha()"""
# El método isalpha() es más especializado, se interesa en letras solamente.

# Ejemplo 1: Demostración del método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())
        # True
        # False


"""El método isdigit()"""
# Al contrario, el método isdigit() busca solo dígitos - cualquier otra cosa produce False(falso) como resultado.

# Ejemplo 2: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())
    # True
    # False


print("Cocodrilo 2".isalpha())
    # False
print("Cocodrilo".isalpha())
    # True
print("Cocodrilo dos".isalpha())
    # False
print("458725 254".isdigit())
    # False
print("458725254".isdigit())
    # True