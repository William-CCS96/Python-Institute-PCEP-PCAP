"""Trabajando con módulos estándar"""
# Antes de comenzar a revisar algunos módulos estándar de Python, veamos la función dir(). No tiene nada que ver con el comando dir de las terminales de Windows o Unix. El comando dir() no muestra el contenido de un directorio o carpeta de disco, pero no se puede negar que hace algo similar: puede revelar todos los nombres proporcionados a través de un módulo en particular.

# Existe una condición: el módulo debe haberse importado previamente como un todo (es decir, utilizar la instrucción import module - from module no es suficiente).

# La función devuelve una lista ordenada alfabéticamente la cual contiene todos los nombres de las entidades disponibles en el módulo:

dir(module)

# Nota: Si el nombre del módulo tiene un alias, debes usar el alias, no el nombre original.
# Usar la función dentro de un script normal no tiene mucho sentido, pero aún así, es posible.
# Por ejemplo, se puede ejecutar el siguiente código para imprimir los nombres de todas las entidades dentro del módulo math:

import math

for name in dir(math):
    print(name, end="\t")

# El código del ejemplo debería producir el siguiente resultado:

# __doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	atan2	atanh	ceil	copysign	cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	factorial	floor	fmod	frexp	fsum	gamma	hypot	isfinite	isinf	isnan	ldexp	lgamma	log	log10	log1p	log2	modf	pi	pow	radians	sin	sinh	sqrt	tan	tanh	trunc	

# ¿Has notado los nombres extraños que comienzan con __ al inicio de la lista? Se hablará más sobre ellos cuando hablemos sobre los problemas relacionados con la escritura de módulos propios.

# Algunos de los nombres pueden traer recuerdos de las lecciones de matemáticas, y probablemente no tendrás ningún problema en adivinar su significado.

# El emplear la función dir() dentro de un código puede no parecer muy útil; por lo general, se desea conocer el contenido de un módulo en particular antes de escribir y ejecutar el código.

# Afortunadamente, se puede ejecutar la función directamente en la consola de Python (IDLE), sin necesidad de escribir y ejecutar un script por separado.

# Así es como se puede hacer:

import math
print(dir(math))