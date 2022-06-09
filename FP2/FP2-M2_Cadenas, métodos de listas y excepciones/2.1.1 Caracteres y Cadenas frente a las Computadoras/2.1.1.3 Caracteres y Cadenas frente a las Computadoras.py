"""# Unicode"""
# Las páginas de códigos ayudaron a la industria informática a resolver problemas de I18N durante algún tiempo, pero pronto resultó que no serían una solución permanente.

# El concepto que resolvió el problema a largo plazo fue el Unicode.

# UNICODE

# Unicode asigna caracteres únicos (letras, guiones, ideogramas, etc.) a más de un millón de puntos de código. Los primeros 128 puntos de código Unicode son idénticos a ASCII, y los primeros 256 puntos de código Unicode son idénticos a la página de códigos ISO/IEC 8859-1 (una página de códigos diseñada para idiomas de Europa occidental).

# UCS-4
# El estándar Unicode no dice nada sobre como codificar y almacenar los caracteres en la memoria y los archivos. Solo nombra todos los caracteres disponibles y los asigna a planos (un grupo de caracteres de origen, aplicación o naturaleza similares).

"""# UCS-4"""

# Existe más de un estándar que describe las técnicas utilizadas para implementar Unicode en computadoras y sistemas de almacenamiento informáticos reales. El más general de ellos es UCS-4.

# El nombre proviene de Universal Character Set (Conjunto de Caracteres Universales).

# UCS-4 emplea 32 bits (cuatro bytes) para almacenar cada carácter, y el código es solo el número único de los puntos de código Unicode. Un archivo que contiene texto codificado UCS-4 puede comenzar con un BOM (byte order mark - marca de orden de bytes), una combinación no imprimible de bits que anuncia la naturaleza del contenido del archivo. Algunas utilidades pueden requerirlo.


# Como puedes ver, UCS-4 es un estándar bastante derrochador: aumenta el tamaño de un texto cuatro veces en comparación con el estándar ASCII. Afortunadamente, hay formas más inteligentes de codificar textos Unicode.

"""# UTF-8"""
# Uno de los más utilizados es UTF-8.

# El nombre se deriva de Unicode Transformation Format (Formato de Transformación Unicode).

# El concepto es muy inteligente. UTF-8 emplea tantos bits para cada uno de los puntos de código como realmente necesita para representarlos.

# UTF-8 - gráficos humorísticos

# Por ejemplo:

# Todos los caracteres latinos (y todos los caracteres ASCII estándar) ocupan ocho bits.
# Los caracteres no latinos ocupan 16 bits.
# Los ideógrafos CJK (China-Japón-Corea) ocupan 24 bits.
# Debido a las características del método utilizado por UTF-8 para almacenar los puntos de código, no es necesario usar el BOM, pero algunas de las herramientas lo buscan al leer el archivo, y muchos editores lo configuran durante el guardado.

# Python 3 es totalmente compatible con Unicode y UTF-8:

# Puedes usar caracteres codificados Unicode / UTF-8 para nombrar variables y otras entidades.
# Puedes usarlos durante todas las entradas y salidas.
# Esto significa que Python3 está completamente Internacionalizado.