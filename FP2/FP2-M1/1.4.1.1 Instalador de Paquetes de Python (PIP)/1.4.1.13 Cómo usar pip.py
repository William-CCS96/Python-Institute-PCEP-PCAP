# Cómo usar pip: continuación
# Suponiendo que tu búsqueda es exitosa (o estás decidido a instalar un paquete específico de un nombre ya conocido), puedes usar pip para instalar el paquete en tu computadora.

# Es posible que ahora se pongan en práctica dos escenarios posibles:

# Deseas instalar un nuevo paquete solo para ti; no estará disponible para ningún otro usuario (cuenta) existente en tu computadora; este procedimiento es el único disponible si no puedes elevar tus permisos y actuar como administrador del sistema.
# Has decidido instalar un nuevo paquete para todo el sistema; tienes privilegios de administrador y no tienes miedo de utilizarlos.
# Para distinguir entre estas dos acciones, pip emplea una opción dedicada llamada --user (observa el guión doble). La presencia de esta opción indica a pip que actúe localmente en nombre de tu usuario sin privilegios de administrador.

# Si no agregas esto, pip asume que eres un administrador del sistema y no hará nada para corregirlo si no lo eres.

# En nuestro caso, vamos a instalar un paquete llamado pygame: es una biblioteca extendida y compleja que permite a los programadores desarrollar juegos de computadora usando Python.

# El proyecto ha estado en desarrollo desde el año 2000, por lo que es un código maduro y confiable. Si quieres saber más sobre el proyecto y sobre la comunidad que lo lidera, visita https://www.pygame.org.

# Si eres administrador del sistema, puedes instalar pygame usando el siguiente comando:

# pip install pygame



# Si no eres un administrador, o no quieres engordar tu sistema operativo instalando pygame en todo el sistema, puedes instalarlo solo para ti:

# pip install --user pygame


# Depende de ti cuál de los procedimientos anteriores deseas que se lleve a cabo.

# pip install --user pygame

# Pip tiene la costumbre de mostrar animaciones textuales sofisticadas que indican el progreso de la instalación, así que observe la pantalla con atención, ¡no te pierdas el espectáculo! Si el proceso tiene éxito, verás algo como la imagen anteror.

# Te alentamos a usar:

# pip show pygame


# y

# pip list


# para obtener más información sobre lo que realmente sucedió.

