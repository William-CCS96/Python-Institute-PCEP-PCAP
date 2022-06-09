"""Tu primer módulo: paso 11"""
# Es hora de hacer este ejemplo más complejo: hemos asumido aquí que el archivo Python principal se encuentra en la misma carpeta o directorio que el módulo que se va a importar.

# Renunciemos a esta suposición y realicemos el siguiente experimento mental:

#         Estamos utilizando el sistema operativo Windows ® (esta suposición es importante, ya que la forma del nombre del archivo depende de ello).
#         El script principal de Python se encuentra en C:\Users\user\py\progs y se llama main.py.
#         El módulo a importar se encuentra en C:\Users\user\py\modules


# ¿Cómo lidiar con ello?

# Para responder a esta pregunta, tenemos que hablar sobre como Python busca los módulos. Hay una variable especial (en realidad una lista) que almacena todas las ubicaciones (carpetas o directorios) que se buscan para encontrar un módulo que ha sido solicitado por la instrucción import.

# Python examina estas carpetas en el orden en que aparecen en la lista: si el módulo no se puede encontrar en ninguno de estos directorios, la importación falla.

# De lo contrario, se tomará en cuenta la primera carpeta que contenga un módulo con el nombre deseado (si alguna de las carpetas restantes contiene un módulo con ese nombre, se ignorará).

# La variable se llama path (ruta), y es accesible a través del módulo llamado sys. Así es como puedes verificar su valor:

import sys

for p in sys.path:
    print(p)


# Hemos ejecutado el código dentro del directorio C:\User\user y esto es lo que obtenemos:

    # C:\Users\user
    # C:\Users\user\AppData\Local\Programs\Python\Python36-32\python36.zip
    # C:\Users\user\AppData\Local\Programs\Python\Python36-32\DLLs
    # C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib
    # C:\Users\user\AppData\Local\Programs\Python\Python36-32
    # C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages

# Nota: la carpeta en la que comienza la ejecución aparece en el primer elemento de la ruta.

# Ten en cuenta también que: hay un archivo zip listado como uno de los elementos de la ruta, esto no es un error. Python puede tratar los archivos zip como carpetas ordinarias, esto puede ahorrar mucho almacenamiento.

# ¿Puedes predecir cómo resolver este problema? Puedes resolverlo agregando una carpeta que contenga el módulo a la variable de ruta (la variable path), es completamente modificable.

"""Tu primer módulo: paso 12"""
# Una de las varias soluciones posibles se ve así:

from sys import path

path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

# Nota:
# Se ha duplicado la \ dentro del nombre de la carpeta, ¿sabes por qué?
#         Debido a que una diagonal invertida se usa para escapar de otros caracteres, si deseas obtener solo una diagonal invertida, debes escapar.

# Hemos utilizado el nombre relativo de la carpeta: esto funcionará si inicia el archivo main.py directamente desde la carpeta de inicio, y no funcionará si el directorio actual no se ajusta a la ruta relativa; siempre puedes usar una ruta absoluta, como esta:
path.append('C:\\Users\\user\\py\\modules')

# Hemos usado el método append(), la nueva ruta ocupará el último elemento en la lista de rutas; si no te gusta la idea, puedes usar en lugar de ello el método insert().
