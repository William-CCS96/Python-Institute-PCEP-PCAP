"""Importando un módulo: continuación"""
# Si necesitas cambiar la palabra math, puedes introducir tu propio nombre, como en el ejemplo:

import math as m
print(m.sin(m.pi/2))

# Nota: después de la ejecución exitosa de una importación con alias, el nombre original del módulo se vuelve inaccesible y no debe ser utilizado.


# A su vez, cuando usa la variante from module import name y se necesita cambiar el nombre de la entidad, se crea un alias para la entidad. Esto hará que el nombre sea reemplazado por el alias que se elija.

# Así es como se puede hacer:

from module import name as alias

# Como anteriormente, el nombre original (sin alias) se vuelve inaccesible.

# La frase name as alias puede repetirse: puedes emplear comas para separar las frases, como a continuación:

from module import n as a, m as b, o as c

# El ejemplo puede parecer un poco extraño, pero funciona:

from math import pi as PI, sin as sine
print(sine(PI/2))

# Ahora estás familiarizado con los conceptos básicos del uso de módulos. Permítenos mostrarte algunos módulos y algunas de sus entidades útiles.