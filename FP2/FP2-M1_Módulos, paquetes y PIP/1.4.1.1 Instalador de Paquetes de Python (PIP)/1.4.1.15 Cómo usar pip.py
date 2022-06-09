# Cómo usar pip: continuación
# Esto es lo que esperamos de nuestro código:

# Símbolo del sistema - python testpg.py


# El comando pip install tiene dos habilidades adicionales importantes:

# Es capaz de actualizar un paquete instalado localmente; por ejemplo, si deseas asegurarte de que estás utilizando la última versión de un paquete en particular, puedes ejecutar el siguiente comando:

# pip install -U nombre_del_paquete


# Donde -U significa actualizar. Nota: esta forma del comando hace uso de la opción --user por el mismo propósito que se presentó anteriormente.

# Es capaz de instalar una versión seleccionada por el usuario de un paquete (pip instala por defecto la versión más nueva disponible); para lograr este objetivo debes utilizar la siguiente sintaxis:

# pip install nombre_del_paquete==versión_del_paquete


# (toma en cuenta el doble signo de igual), por ejemplo:

# pip install pygame==1.9.2