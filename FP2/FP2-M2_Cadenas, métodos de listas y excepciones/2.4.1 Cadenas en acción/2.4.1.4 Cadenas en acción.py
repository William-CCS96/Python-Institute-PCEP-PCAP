"""Cadenas frente a números"""
# Hay dos cuestiones adicionales que deberían discutirse aquí: ¿Cómo convertir un número (un entero o un flotante) en una cadena, y viceversa? Puede ser necesario realizar tal transformación. Además, es una forma rutinaria de procesar datos de entrada o salida.
# La conversión de cadena a número es simple, ya que siempre es posible. Se realiza mediante una función llamada str().
# Justo como aquí:

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
    # 13 1.3

# La transformación inversa solo es posible cuando la cadena representa un número válido. Si no se cumple la condición, espera una excepción ValueError.
# Emplea la función int() si deseas obtener un entero, y float() si necesitas un valor punto flotante.

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
    # 14.3

# En la siguiente sección, te mostraremos algunos programas simples que procesan cadenas.