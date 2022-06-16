"""El método endswith()"""
# El método endswith() comprueba si la cadena dada termina con el argumento especificado y devuelve True(verdadero) o False(falso), dependiendo del resultado.

# Nota: la subcadena debe adherirse al último carácter de la cadena; no se puede ubicar en algún lugar cerca del final de la cadena.

# Observa el ejemplo en el editor, analízalo y ejecútalo. Su salida es:
# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
# si

# Ahora deberías poder predecir la salida del fragmento de código a continuación:

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
# True
# False
# False
# True



