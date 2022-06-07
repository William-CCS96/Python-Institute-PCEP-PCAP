flag_register = 0x1234
#La variable almacena la información sobre varios aspectos de la operación del sistema. Cada bit de la variable almacena un valor de si/no. También se te ha dicho que solo uno de estos bits es tuyo, el tercero (recuerda que los bits se numeran desde cero y el número de bits cero es el más bajo, mientras que el más alto es el número 31). Los bits restantes no pueden cambiar, porque están destinados a almacenar otros datos. Aquí está tu bit marcado con la letra x:
flag_register = 0000000000000000000000000000x000
#1. Comprobar el estado de tu bit: deseas averiguar el valor de su bit; comparar la variable completa con cero no hará nada, porque los bits restantes pueden tener valores completamente impredecibles, pero puedes usar la siguiente propiedad de conjunción:

x & 1 = x
x & 0 = 0

#(observa el 1 en la posición de tu bit) como resultado, obtendrás una de las siguientes cadenas de bits:
00000000000000000000000000001000 #si tu bit se estableció en 1
00000000000000000000000000000000 #si tu bit se reseteo a 0

#Dicha secuencia de ceros y unos, cuya tarea es tomar el valor o cambiar los bits seleccionados, se denomina máscara de bits
#Construyamos una máscara de bits para detectar el estado de tus bits. Debería apuntar a el tercer bit. Ese bit tiene el peso de 23=8. Se podría crear una máscara adecuada mediante la siguiente sentencia:

the_mask = 8
#También puedes hacer una secuencia de instrucciones dependiendo del estado de tu bit, aquí está:
if flag_register & the_mask:
    # Mi bit se estableció en 1.
else:
    # Mi bit se restableció a 0.

#2. Reinicia tu bit
#asigna un cero al bit, mientras que todos los otros bits deben permanecer sin cambios;
11111111111111111111111111110111
#Tenga en cuenta que la máscara se creó como resultado de la negación de todos los bits de la variable the_mask. Restablecer el bit es simple, y se ve así (elige el que más te guste):Restablecer el bit es simple, y se ve así (elige el que más te guste):

flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

#3. Establece tu bit : asigna un 1 a tu bit, mientras que todos los bits restantes deben permanecer sin cambios; usa la siguiente propiedad de disyunción:
x | 1 = 1
x | 0 = x

#Ya estás listo para configurar su bit con una de las siguientes instrucciones:

flag_register = flag_register | the_mask
flag_register |= the_mask

#4. Niega tu bit: reemplaza un 1 con un 0 y un 0 con un 1. Puedes utilizar una propiedad interesante del operador ~x:
x ^ 1 = ~x
x ^ 0 = x

#Niega tu bit con las siguientes instrucciones:

flag_register = flag_register ^ the_mask
flag_register ^= the_mask
