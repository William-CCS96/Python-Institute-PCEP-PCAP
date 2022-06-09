# Cómo usar pip: continuación
# La lista pip no es muy informativa y puede suceder que no satisfaga tu curiosidad. Afortunadamente, hay un comando que puede brindarte más información sobre cualquiera de los paquetes instalados (ten en cuenta la palabra installed). La sintaxis del comando es la siguiente:

# pip show nombre_del_paquete


# Lo usaremos de una manera un poco engañosa: queremos convencer a pip de que confiese algo sobre sí mismo. Así es como lo hacemos:

# pip show pip


# Parece un poco extraño, ¿no? A pesar de esto, funciona bien y la autopresentación de pip parece consistente y actual:

# pip show pip

# ¿Puedes preguntar de dónde provienen estos datos? ¿Es pip realmente tan perceptivo? En lo absoluto: la información que aparece en la pantalla se toma del interior del paquete que se muestra. En otras palabras, el creador del paquete está obligado a equiparlo con todos los datos necesarios (o para expresarlo de manera más precisa: metadatos).

# Observa las dos líneas en la parte inferior de la salida. Muestran:

# Qué paquetes son necesarios para utilizar con éxito el paquete (Requires:).
# Qué paquetes necesitan que el paquete se utilice con éxito (Required-by:).
# Como puedes ver, ambas propiedades están vacías. No dudes en intentar utilizar el comando show en relación con cualquier otro paquete instalado.




# El poder de pip proviene del hecho de que en realidad es una puerta de entrada al universo del software Python. Gracias a eso, puedes navegar e instalar cualquiera de los cientos de paquetes listos para usar reunidos en los repositorios de PyPI. No olvides que pip no puede almacenar todo el contenido de PyPI localmente (es innecesario y no sería económico).

# De hecho, pip usa Internet para consultar PyPI y descargar los datos requeridos. Esto significa que debes tener una conexión de red en funcionamiento siempre que vayas a solicitar a pip cualquier cosa que pueda implicar interacciones directas con la infraestructura de PyPI.

# Uno de estos casos ocurre cuando deseas buscar en PyPI para encontrar el paquete deseado. Este tipo de búsqueda se inicia con el siguiente comando:

# pip search anystring


# La cadena anystring que se proporciono será buscada en:

# Los nombres de todos los paquetes.
# Las cadenas de resumen de todos los paquetes.
# Ten en cuenta que algunas búsquedas pueden generar una avalancha real de datos, así que trata de ser lo más específico posible. Por ejemplo, una consulta de apariencia inocente como esta:

# pip search pip


# Produce más de 100 líneas de resultados (pruébalo tu mismo, no te fíes de nuestra palabra). Por cierto, la búsqueda no distingue entre mayúsculas y minúsculas.

# Si no eres fanático de la lectura en consola, puedes usar la forma alternativa de navegar por el contenido de PyPI que ofrece un motor de búsqueda, disponible en https://pypi.org/search.