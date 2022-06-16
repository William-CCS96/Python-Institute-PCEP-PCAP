"""El método isalnum()"""
# El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True(verdadero) o False(falso) de acuerdo al resultado.

# Observa el ejemplo en el editor y ejecútalo.

# Nota: cualquier elemento de cadena que no sea un dígito o una letra hace que el método regrese False(falso). Una cadena vacía también lo hace.

# Demostración del método the isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
    # True
    # True
    # True
    # False
    # False
    # False

# Existen tres ejemplos más aquí:

t = 'Six lambdas'
print(t.isalnum())
    #False
t = 'ΑβΓδ'
print(t.isalnum())
    # True
t = '20E1'
print(t.isalnum())
    # True

# Ejecútalos y verifica su salida.
# Nota: la causa del primer resultado es un espacio, no es ni un dígito ni una letra.

