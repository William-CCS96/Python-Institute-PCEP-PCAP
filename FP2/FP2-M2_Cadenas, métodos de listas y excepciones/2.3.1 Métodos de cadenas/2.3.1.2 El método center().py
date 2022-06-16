"""El método center()"""
# La variante de un parámetro del método center() genera una copia de la cadena original, tratando de centrarla dentro de un campo de un ancho especificado.

# El centrado se realiza realmente al agregar algunos espacios antes y después de la cadena.

# No esperes que este método demuestre habilidades sofisticadas. Es bastante simple.

# El ejemplo en el editor usa corchetes para mostrar claramente donde comienza y termina realmente la cadena centrada.
# Su salida se ve de la siguiente manera:
# Demostración del método center():

print('[' + 'alpha'.center(10) + ']')
# [  alpha   ]

# Si la longitud del campo de destino es demasiado pequeña para ajustarse a la cadena, se devuelve la cadena original.
# Puedes ver el método center() en más ejemplos aquí:

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'Beta'.center(7) + ']')
# [Beta]
# [Beta]
# [ Beta ]
# [  Beta ]

# Ejecuta el código anterior y verifica que salidas produce.
# La variante de dos parámetros de center() hace uso del carácter del segundo argumento, en lugar de un espacio. Analiza el siguiente ejemplo:

print('[' + 'gamma'.center(20, '*') + ']')
# [*******gamma********]

print('[' + 'Coco'.center(12,"-") + ']')
# [----Coco----]

print("["+("Cocoliso"*4).center(40,"*")+"]")
# [****CocolisoCocolisoCocolisoCocoliso****]


