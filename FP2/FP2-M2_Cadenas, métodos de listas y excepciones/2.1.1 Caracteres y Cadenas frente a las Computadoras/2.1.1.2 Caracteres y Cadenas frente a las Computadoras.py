# I18N
# Ahora, el alfabeto latino no es suficiente para toda la humanidad. Los usuarios de ese alfabeto son minoría. Era necesario idear algo más flexible y capaz que ASCII, algo capaz de hacer que todo el software del mundo sea susceptible de internacionalización, porque diferentes idiomas usan alfabetos completamente diferentes, y a veces estos alfabetos no son tan simples como el latino.

# La palabra internacionalización se acorta comúnmente a I18N.

# I18N Internacionalización

# ¿Por qué? Observa con cuidado, hay una I al inicio de la palabra, a continuación hay 18 letras diferentes, y una N al final.

# A pesar del origen ligeramente humorístico, el término se utiliza oficialmente en muchos documentos y normas.

# El software I18N es un estándar en los tiempos actuales. Cada programa tiene que ser escrito de una manera que permita su uso en todo el mundo, entre diferentes culturas, idiomas y alfabetos.

# El código ASCII emplea ocho bits para cada signo. Ocho bits significan 256 caracteres diferentes. Los primeros 128 se usan para el alfabeto latino estándar (tanto en mayúsculas como en minúsculas). ¿Es posible colocar todos los otros caracteres utilizados en todo el mundo a los 128 lugares restantes?

# No, no lo es.



# Puntos de código y páginas de códigos
# Necesitamos un nuevo término: un punto de código.

# Un punto de código es un numero que compone un caracter. Por ejemplo, el 32 es un punto de código que compone un espacio en codificación ASCII. Podemos decir que el código ASCII estándar consta de 128 puntos de código.

# Como el ASCII estándar ocupa 128 de 256 puntos de código posibles, solo puedes hacer uso de los 128 restantes.

# No es suficiente para todos los idiomas posibles, pero puede ser suficiente para un idioma o para un pequeño grupo de idiomas similares.

# ¿Se puede establecer la mitad superior de los puntos de código de manera diferente para diferentes idiomas? Si, por supuesto. A tal concepto se le denomina una página de códigos.

# Una página de códigos es un estándar para usar los 128 puntos de código superiores para almacenar caracteres específicos. Por ejemplo, hay diferentes páginas de códigos para Europa Occidental y Europa del Este, alfabetos cirílicos y griegos, idiomas árabe y hebreo, etc.

# Esto significa que el mismo punto de código puede formar diferentes caracteres cuando se usa en diferentes páginas de códigos.

# Por ejemplo, el punto de código 200 forma una Č (una letra usada por algunas lenguas eslavas) cuando lo utiliza la página de códigos ISO/IEC 8859-2, pero forma un Ш (una letra cirílica) cuando es usado por la página de códigos ISO/IEC 8859-5.

# En consecuencia, para determinar el significado de un punto de código específico, debes conocer la página de códigos de destino.

# En otras palabras, los puntos de código derivados del código de páginas son ambiguos.