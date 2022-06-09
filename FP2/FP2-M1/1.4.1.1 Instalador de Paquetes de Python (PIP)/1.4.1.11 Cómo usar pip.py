# Cómo usar pip
# Ahora estamos listos para preguntarle a pip qué puede hacer por nosotros. Hagámoslo, emite el siguiente comando:

# pip help


# y espera la respuesta de pip. Así es como se mira:

# pip help

# No olvides que puedes necesitar reemplazar pip por pip3 si tu entorno lo requiere.

# La lista producida por pip resume todas las operaciones disponibles, y la última de ellas es help, la cual acabamos de usar.

# Si deseas saber más sobre cualquiera de las operaciones enumeradas, puedes utilizar la siguiente forma de invocación de pip:

# pip help (operación o comando)



# Por ejemplo, la línea:
# pip help install


# te mostrará información detallada sobre el uso y la parametrización del comando install.

# Si deseas saber qué paquetes de Python se han instalado hasta ahora, puedes usar la operación list, justo como aquí:

# pip list


# El resultado que verás es bastante impredecible. No te sorprendas si el contenido de tu pantalla termina siendo completamente diferente. El nuestro es el siguiente:

# pip list

# Como puedes ver, hay dos columnas en la lista, una muestra el nombre del paquete instalado y la otra muestra la versión del paquete. No podemos predecir el estado de tu instalación de Python.

# Lo único que sabemos con certeza es que tu lista contiene las dos líneas que vemos en nuestra lista: pip y setuptools. Esto sucede porque el sistema operativo está convencido de que un usuario que desee pip probablemente necesitará las setuptools (herramientas de configuración). No está mal.