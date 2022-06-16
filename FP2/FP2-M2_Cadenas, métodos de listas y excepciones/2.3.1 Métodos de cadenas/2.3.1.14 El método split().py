"""El método split()"""
# El método split() divide la cadena y crea una lista de todas las subcadenas detectadas.

# El método asume que las subcadenas están delimitadas por espacios en blanco - los espacios no participan en la operación y no se copian en la lista resultante.

# Si la cadena está vacía, la lista resultante también está vacía.

# Observa el código en el editor. El ejemplo produce el siguiente resultado:

# Demostración del método split():
print("phi       chi\npsi".split())
    # ['phi', 'chi', 'psi']

# Nota: la operación inversa se puede realizar por el método join().

print("hola a todos .".split())
    # ['hola', 'a', 'todos', '.']


#--------------- 
"""Ejercicio 1"""
# ¿Cuál de las siguientes líneas describe una condición verdadera?

'smith' > 'Smith'
'Smiths' < 'Smith'
'Smith' > '1000'
'11' < '8'

    # 1, 3 y 4

"""Ejercicio 2"""
# ¿Cuál es el resultado esperado del siguiente código?

s1 = '¿Dónde están las nevadas de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])
    # de

"""Ejercicio 3"""
# ¿Cuál es el resultado esperado del siguiente código?
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)
# El código genera una excepción ValueError

