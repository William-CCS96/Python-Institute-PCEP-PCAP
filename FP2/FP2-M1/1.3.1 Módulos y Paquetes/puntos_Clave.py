"""Puntos Clave"""

# 1. Mientras que un módulo está diseñado para acoplar algunas entidades relacionadas como funciones, variables o constantes, un paquete es un contenedor que permite el acoplamiento de varios módulos relacionados bajo un mismo nombre. Dicho contenedor se puede distribuir tal cual (como un lote de archivos implementados en un subárbol de directorio) o se puede empaquetar dentro de un archivo zip.


# 2. Durante la primera importación del módulo, Python traduce su código fuente a un formato semi-compilado almacenado dentro de los archivos pyc y los implementa en el directorio __pycache__ ubicado en el directorio de inicio del módulo.


# 3. Si deseas decirle al usuario del módulo que una entidad en particular debe tratarse como privada (es decir, no debe usarse explícitamente fuera del módulo), puedes marcar su nombre con el prefijo _ o __. No olvides que esto es solo una recomendación, no una orden.


# 4. Los nombres shabang, shebang, hasbang, poundbang y hashpling describen el dígrafo escrito como #!, se utiliza para instruir a los sistemas operativos similares a Unix sobre cómo se debe iniciar el archivo fuente de Python. Esta convención no tiene efecto en MS Windows.


# 5. Si deseas convencer a Python de que debe tomar en cuenta el directorio de un paquete no estándar, su nombre debe insertarse/agregarse en/a la lista de directorios de importación almacenada en la variable path contenida en el módulo sys.


# 6. Un archivo de Python llamado __init__.py se ejecuta implícitamente cuando un paquete que lo contiene está sujeto a importación y se utiliza para inicializar un paquete y/o sus subpaquetes (si los hay). El archivo puede estar vacío, pero no debe faltar.

#------------
"""Ejercicio 1"""
# Deseas evitar que el usuario de tu módulo ejecute tu código como un script ordinario. ¿Cómo lograrías tal efecto?

import sys

if __name__ == "__main__":
    print "¡No hagas eso!"
    sys.exit()

"""Ejercicio 2"""
# Algunos paquetes adicionales y necesarios se almacenan dentro del directorio D:\Python\Project\Modules. Escribe un código asegurándote de que Python recorra el directorio para encontrar todos los módulos solicitados.

import sys

# ¡Toma en cuenta las diagonales invertidas dobles!
sys.path.append("D:\\Python\\Project\\Modules")

"""Ejercicio 3"""
# El directorio mencionado en el ejercicio anterior contiene un subárbol con la siguiente estructura:

abc
 |__ def
      |__ mymodule.py

# Asumiendo que D:\Python\Project\Modules se ha adjuntado con éxito a la lista sys.path, escribe una directiva de importación que te permita usar todas las entidades de mymodule.

import abc.def.mymodule


