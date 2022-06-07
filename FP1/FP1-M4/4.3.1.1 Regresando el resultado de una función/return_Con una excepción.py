    # def function():
    #     return expression

# Provoca la terminación inmediata de la ejecución de la función (nada nuevo en comparación con la primer variante).
# Además, la función evaluará el valor de la expresión y lo devolverá (de ahí el nombre una vez más) como el resultado de la función.

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)
    # La función boring_function ha devuelto su resultado. Es: 123

# Ten en cuenta que no estamos siendo muy educados aquí: la función devuelve un valor y lo ignoramos (no lo usamos de ninguna manera):

def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")
    # ¡Esta lección es interesante!
    # 'Modo aburrimiento' ON.
    # Esta lección es aburrida...
