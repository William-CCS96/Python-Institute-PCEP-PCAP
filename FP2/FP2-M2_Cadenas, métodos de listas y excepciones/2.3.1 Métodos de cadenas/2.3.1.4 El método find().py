"""El método find()"""
# El método find() es similar al método index(), el cual ya conoces - busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:

# Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
# Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.
# Analiza el código en el editor. Así es como puedes usarlo.

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))
    # 1
    # -1

# Nota: no se debe de emplear find() si deseas verificar si un solo carácter aparece dentro de una cadena - el operador in será significativamente más rápido.

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
    # 2
    # 2
    # 0
    # -1

# Si deseas realizar la búsqueda, no desde el principio de la cadena, sino desde cualquier posición, puedes usar una variante de dos parámetros del método find(). Mira el ejemplo:

print('kappa'.find('a', 2))
    # 4
# El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que estar dentro de la cadena).
# De las dos letras a, solo se encontrará la segunda. Ejecuta el código y verifica.

# Se puede emplear el método find() para buscar todas las ocurrencias de la subcadena, como aquí:

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    # 15
    # 80
    # 198
    # 221
    # 238

# Existe también una mutación de tres parámetros del método find() - el tercer argumento apunta al primer índice que no se tendrá en cuenta durante la búsqueda (en realidad es el límite superior de la búsqueda).
# Observa el ejemplo a continuación:

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que estar dentro de la cadena).
# Por lo tanto, las salidas de ejemplo son:

        # 1
        # -1
# a no se puede encontrar dentro de los límites de búsqueda dados en el segundo print().

print("William".find("ll"))
print("William".find("l"))
    # 2
    # 2
print("Camilo".find("i",2))
    # 3
print("Camilo".find("i",4))  
    # -1

