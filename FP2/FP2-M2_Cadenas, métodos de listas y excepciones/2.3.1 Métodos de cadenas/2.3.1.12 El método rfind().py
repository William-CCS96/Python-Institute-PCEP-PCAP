"""El método rfind()"""
# Los métodos de uno, dos y tres parámetros denominados rfind() hacen casi lo mismo que sus contrapartes (las que carecen del prefijo r), pero comienzan sus búsquedas desde el final de la cadena, no el principio (de ahí el prefijo r, de reversa).

# Echa un vistazo al código en el editor e intenta predecir su salida. Ejecuta el código para verificar si tenías razón.

# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
    # 8
    # -1
    # 4

print("tau tau tau".count("ta"))
