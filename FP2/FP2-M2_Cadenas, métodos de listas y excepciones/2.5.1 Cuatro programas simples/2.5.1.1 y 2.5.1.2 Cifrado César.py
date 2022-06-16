"""El Cifrado César: encriptando un mensaje"""
# Te mostraremos cuatro programas simples para presentar algunos aspectos del procesamiento de cadenas en Python. Son intencionalmente simples, pero los problemas de laboratorio serán significativamente más complicados.

# El primer problema que queremos mostrarte se llama Cifrado César - más detalles aquí: https://en.wikipedia.org/wiki/Caesar_cipher.

# Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César y sus tropas durante las Guerras Galas. La idea es bastante simple: cada letra del mensaje se reemplaza por su consecuente más cercano (A se convierte en B, B se convierte en C, y así sucesivamente). La única excepción es la Z, la cual se convierte en A.

# El programa en el editor es una implementación muy simple (pero funcional) del algoritmo.
# Se ha escrito utilizando los siguientes supuestos:

    # Solo acepta letras latinas (nota: los Romanos no usaban espacios en blanco ni dígitos).
    # Todas las letras del mensaje están en mayúsculas (nota: los Romanos solo conocían las mayúsculas).
# Veamos el código:

    # La línea 02: pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
    # La línea 03: prepara una cadena para el mensaje cifrado (esta vacía por ahora).
    # La línea 04: inicia la iteración a través del mensaje.
    # La línea 05: si el carácter actual no es alfabético...
    # La línea 06: ...ignoralo.
    # La línea 07: convierta la letra a mayúsculas (es preferible hacerlo a ciegas, en lugar de verificar si es necesario o no).
    # La línea 08: obtén el código de la letra e increméntalo en uno.
    # La línea 09: si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
    # La línea 10: ... cámbialo al código de la A.
    # La línea 11: agrega el carácter recibido al final del mensaje cifrado.
    # La línea 13: imprime el cifrado.

# El código, con este mensaje:
# AVE CAESAR

# Da como salida:
# BWFDBFTBS



text=input("Introduce el texto: ")
cipher=""

for char in text:
    if not char.isalpha():
        continue
    char=char.upper()
    code=ord(char)+1
    if code>ord("Z"):
        code=ord("A")
    cipher+=chr(code)

print(cipher)
# IPMBNVOEPNVOEBOP

text2=input("Introduce el cifrado: ")
cipher2=""
for char in text2:
    if not char.isalpha():
        continue
    char=char.upper()
    code=ord(char)-1
    if code<ord("A"):
        code=ord("Z")
    cipher2+=chr(code)

print(cipher2) 
# HOLAMUNDOMUNDANO


