"""El método lstrip()"""
# El método sin parámetros lstrip() devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.

# Analiza el ejemplo en el editor.
# Demostración del método the lstrip():
print("[" + " tau ".lstrip() + "]")
    # [tau ]

# Los corchetes no son parte del resultado, solo muestran los límites del resultado.

# El método con un parámetro lstrip() hace lo mismo que su versión sin parámetros, pero elimina todos los caracteres incluidos en el argumento (una cadena), no solo espacios en blanco:

print("www.cisco.com".lstrip("w."))
    # cisco.com

# ¿Puedes adivinar la salida del fragmento a continuación? Piensa cuidadosamente. Ejecuta el código y verifica tus predicciones.
print("pythoninstitute.org".lstrip(".org"))

print("hhola".lstrip("h"))
    # ola
print("  hola".lstrip("h"))
    #   hola
print("  hola".lstrip())
    # hola