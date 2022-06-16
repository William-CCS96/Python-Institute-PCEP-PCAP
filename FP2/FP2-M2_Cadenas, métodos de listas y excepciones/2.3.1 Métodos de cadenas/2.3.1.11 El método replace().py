"""El método replace()"""
# El método replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
    # www.pythoninstitute.org
    # Thare are it!
    # Apple

# Si el segundo argumento es una cadena vacía, reemplazar significa realmente eliminar el primer argumento de la cadena. ¿Qué tipo de magia ocurre si el primer argumento es una cadena vacía?
print("Hola mundi a todos".replace("","-"))
    # -H-o-l-a- -m-u-n-d-i- -a- -t-o-d-o-s-
print("Hola mundi a todos".replace("","-",5))
    # -H-o-l-a- mundi a todos

# La variante del método replace() con tres parámetros emplea un tercer argumento (un número) para limitar el número de reemplazos.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
    # Thare is it!
    # Thare are it!


