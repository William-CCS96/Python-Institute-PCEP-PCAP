# Dependencias
# Ahora que estamos seguros de que pip está listo para usarse, vamos a limitar nuestro enfoque a MS Windows solamente, ya que su comportamiento es (debería ser) el mismo en todos los sistemas operativos, pero antes de comenzar, debemos explicar un asunto importante e informarte sobre las dependencias.

# Imagina que has creado una brillante aplicación de Python llamada redsuspenders, capaz de predecir los tipos de cambio de la bolsa de valores con un 99% de precisión (por cierto, si realmente lo haces, contáctanos de inmediato).

# Por supuesto, has utilizado algún código existente para lograr este objetivo, por ejemplo, tu aplicación importa un paquete llamado nyse que contiene algunas funciones y clases cruciales. Además, el paquete nyse importa otro paquete llamado wallstreet, mientras que el paquete wallstreet importa otros dos paquetes esenciales llamados bull y bear.

# Como probablemente ya habrás adivinado, las conexiones entre estos paquetes son cruciales, y si alguien decide usar tu código (pero recuerda, ya lo hemos reclamado primero) también tendrás que asegurarte de que todos los paquetes requeridos están en su lugar.

# Para abreviar, podemos decir que la dependencia es un fenómeno que aparece cada vez que vas a utilizar un software que depende de otro software. Ten en cuenta que la dependencia puede incluir (y generalmente incluye) más de un nivel de desarrollo de software.

# ¿Significa esto que un usuario potencial del paquete nyse está obligado a rastrear todas las dependencias e instalar manualmente todos los paquetes necesarios? Eso sería horrible, ¿no?

# Sí, definitivamente es horrible, por lo que no deberías sorprenderse de que el proceso de cumplir arduamente con todos los requisitos posteriores tenga su propio nombre, y se llame infierno de dependencias.

# ¿Cómo nos ocupamos de eso? ¿Todos los usuarios están condenados a visitar el infierno para ejecutar el código por primera vez?

# Afortunadamente no, pip puede hacer todo esto por ti. Puede descubrir, identificar y resolver todas las dependencias. Además, puede hacerlo de la manera más inteligente, evitando descargas y reinstalaciones innecesarias.

