"""Tu primer módulo: paso 3"""
# Ahora hemos puesto algo en el archivo del módulo:

# print("Me gusta ser un módulo.")

# ¿Puedes notar alguna diferencia entre un módulo y un script ordinario? No hay ninguna hasta ahora.
# Es posible ejecutar este archivo como cualquier otro script. Pruébalo por ti mismo.
# ¿Qué es lo que pasa? Deberías de ver la siguiente línea dentro de tu consola:

# Me gusta ser un módulo.

"""Tu primer módulo: paso 4"""
# Volvamos al archivo main.py:

# Ejecuta el archivo. ¿Qué ves? Con suerte, verás algo como esto:
# Me gusta ser un módulo.

# ¿Qué significa realmente?

# Cuando un módulo es importado, su contenido es ejecutado implícitamente por Python. Le da al módulo la oportunidad de inicializar algunos de sus aspectos internos (por ejemplo, puede asignar a algunas variables valores útiles).

# Nota: la inicialización se realiza sólo una vez, cuando se produce la primera importación, por lo que las asignaciones realizadas por el módulo no se repiten innecesariamente.

# Imagina el siguiente contexto:

#         Existe un módulo llamado mod1.
#         Existe un módulo llamado mod2 el cual contiene la instrucción import mod1.
#         Hay un archivo principal que contiene las instrucciones import mod1 e import mod2.
# A primera vista, se puede pensar que mod1 será importado dos veces - afortunadamente, solo se produce la primera importación. Python recuerda los módulos importados y omite silenciosamente todas las importaciones posteriores.

"""Tu primer módulo: paso 5"""
# Python puede hacer mucho más que solo importar el módulo. También crea una variable llamada __name__.
# Además, cada archivo fuente usa su propia versión separada de la variable, no se comparte entre módulos.
# Te mostraremos como usarlo. Modifica el módulo un poco:

# print("Me gusta ser un módulo.")
# print(__name__)

# Ahora ejecuta el archivo module.py. Deberías ver las siguientes líneas:

# Me gusta ser un módulo.
# __main__

# Ahora ejecuta el archivo main.py. ¿Y? ¿Ves lo mismo que nosotros?

# Me gusta ser un módulo.
# module


# Podemos decir que:

#         Cuando se ejecuta un archivo directamente, su variable __name__ se establece a __main__.
#         Cuando un archivo se importa como un módulo, su variable __name__ se establece al nombre del archivo (excluyendo a .py).

"""Tu primer módulo: paso 6"""
# Así es como puedes hacer uso de la variable __main__ para detectar el contexto en el cual se activó tu código:

# if __name__ == "__main__":
#     print("Yo prefiero ser un módulo")
# else:
#     print("Me gusta ser un módulo")

# Sin embargo, existe una forma más inteligente de utilizar la variable. Si escribes un módulo lleno de varias funciones complejas, puedes usarla para colocar una serie de pruebas para verificar si las funciones trabajan correctamente.

# Cada vez que modifiques alguna de estas funciones, simplemente puedes ejecutar el módulo para asegurarte de que sus enmiendas no estropeen el código. Estas pruebas se omitirán cuando el código se importe como un módulo.