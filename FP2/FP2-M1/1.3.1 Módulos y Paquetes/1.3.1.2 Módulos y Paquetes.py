"""Tu primer módulo: paso 1"""
# En esta sección, trabajarás localmente en tu máquina. Comencemos desde cero. Crea un archivo vacío, de la siguiente manera:

module.py

# Se necesitan dos archivos para realizar estos experimentos. Uno de ellos será el módulo en sí. Está vacío ahora. No te preocupes, lo vas a llenar con código pronto.

# El archivo lleva por nombre module.py. No muy creativo, pero es simple y claro.

"""
Tu primer módulo: paso 2"""
# El segundo archivo contiene el código que utiliza el nuevo módulo. Su nombre es main.py. Su contenido es muy breve hasta ahora:

# Creando el archivo main.py el cual contiene la instrucción import module
import module

# Nota: ambos archivos deben estar ubicados en la misma carpeta. Te recomendamos crear una carpeta nueva y vacía para ambos archivos. Esto hará que las cosas sean más fáciles.

# Inicia el IDLE (o cualquier otro que prefieras) y ejecuta el archivo main.py. ¿Qué es lo que ves?

# No deberías ver nada. Esto significa que Python ha importado con éxito el contenido del archivo module.py.

# No importa que el módulo esté vacío por ahora. El primer paso ya está hecho, pero antes de dar el siguiente paso, queremos que eches un vistazo a la carpeta en la que se encuentran ambos archivos.

# ¿Notas algo interesante?

# Ha aparecido una nueva subcarpeta, ¿puedes verla? Su nombre es __pycache__. Echa un vistazo adentro. ¿Qué es lo que ves?

# Hay un archivo llamado (más o menos) module.cpython-xy.pyc donde x y y son dígitos derivados de tu versión de Python (por ejemplo, serán 3 y 8 si utilizas Python 3.8).

# El nombre del archivo es el mismo que el de tu módulo. La parte posterior al primer punto dice qué implementación de Python ha creado el archivo (CPython) y su número de versión. La ultima parte (pyc) viene de las palabras Python y compilado.

# Puedes mirar dentro del archivo: el contenido es completamente ilegible para los humanos. Tiene que ser así, ya que el archivo está destinado solo para uso el uso de Python.

# Cuando Python importa un módulo por primera vez, traduce el contenido a una forma algo compilada.

# El archivo no contiene código en lenguaje máquina: es código semi-compilado interno de Python, listo para ser ejecutado por el intérprete de Python. Como tal archivo no requiere tantas comprobaciones como las de un archivo fuente, la ejecución comienza más rápido y también se ejecuta más rápido.

# Gracias a eso, cada importación posterior será más rápida que interpretar el código fuente desde cero.

# Python puede verificar si el archivo fuente del módulo ha sido modificado (en este caso, el archivo pyc será reconstruido) o no (cuando el archivo pyc pueda ser ejecutado al instante). Este proceso es completamente automático y transparente, no tiene que ser tomando en cuenta.z