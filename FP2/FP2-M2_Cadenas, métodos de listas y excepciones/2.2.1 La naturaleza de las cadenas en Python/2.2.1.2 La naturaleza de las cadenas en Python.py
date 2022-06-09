
multiline="""Linea #1
Linea #2"""

print(len(multiline))
    # 18

"""Cadenas multilínea"""
# Ahora es un muy buen momento para mostrarte otra forma de especificar cadenas dentro del código fuente de Python. Ten en cuenta que la sintaxis que ya conoces no te permitirá usar una cadena que ocupe más de una línea de texto.

# Por esta razón, el código siguiente es erróneo:

# multiline = 'Línea #1
# Línea #2'

# print(len(multiline))

# Afortunadamente, para este tipo de cadenas, Python ofrece una sintaxis simple, conveniente y separada.

# Observa el código en el editor. Así es como se ve.

# Como puedes ver, la cadena comienza con tres apóstrofes, no uno. El mismo apóstrofe triplicado se usa para terminar la cadena.

# El número de líneas de texto dentro de una cadena de este tipo es arbitrario.

# La salida del código es 17.

# Cuenta los caracteres con cuidado. ¿Es este resultado correcto o no? Se ve bien a primera vista, pero cuando cuentas los caracteres, no lo es.

# Línea #1 contiene ocho caracteres. Las dos líneas juntas contienen 16 caracteres. ¿Perdimos un carácter? ¿Dónde? ¿Cómo?

# No, no lo hicimos.

# El carácter que falta es simplemente invisible: es un espacio en blanco. Se encuentra entre las dos líneas de texto.

# Se denota como: \n.

# ¿Lo recuerdas? Es un carácter especial (de control) utilizado para forzar un avance de línea. No puedes verlo, pero cuenta.

# Las cadenas multilínea pueden ser delimitadas también por comillas triples, como aqui:

# multiline = """Línea #1
# Línea #2"""

# print(len(multiline))


# Elige el método que sea más cómodo. Ambos funcionan igual.