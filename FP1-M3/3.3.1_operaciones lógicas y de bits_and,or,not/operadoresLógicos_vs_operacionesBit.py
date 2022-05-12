i = 15
j = 22

#Imagen a nivel de bits/ Los enteros se alamacenana en 32 bits

i: 00000000000000000000000000001111
j: 00000000000000000000000000010110

log = i and j
#Ambas variables i y j no son ceros
log: True

#Operación a nivel de bits
bit = i & j

i	        00000000000000000000000000001111
j	        00000000000000000000000000010110
bit = i & j	00000000000000000000000000000110
#Estos bits corresponden al valor entero de seis.

#Operadores de negación

logneg = not i
#La variable logneg se establecerá en False: no es necesario hacer nada más.

#La negación a nivel de bits es así:
bitneg = ~i

i	        00000000000000000000000000001111
bitneg = ~i	11111111111111111111111111110000

