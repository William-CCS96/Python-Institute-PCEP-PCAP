"""Tu primer paquete: paso 3"""
# Así es como se ve el árbol actualmente:

# Tal estructura es casi un paquete (en el sentido de Python). Carece del detalle fino para ser funcional y operativo. Lo completaremos en un momento.

# Si asumes que extra es el nombre de un paquete recientemente creado (piensa en el como la raíz del paquete), impondrá una regla de nomenclatura que te permitirá nombrar claramente cada entidad del árbol.

"""Por ejemplo:"""
# La ubicación de una función llamada funT() del paquete tau puede describirse como:
#         extra.good.best.tau.funT()

# Una función marcada como:
#         extra.ugly.psi.funP()
# Proviene del módulo psi el cual esta almacenado en el subpaquete ugly del paquete extra.

"""Tu primer paquete: paso 4"""
# Ahora se deben responder dos preguntas:

        # ¿Cómo se transforma este árbol (en realidad, un subárbol) en un paquete real de Python (en otras palabras, ¿cómo convence a Python de que dicho árbol no es solo un montón de archivos basura, sino un conjunto de módulos)?
        # ¿Dónde se coloca el subárbol para que Python pueda acceder a él?

# La primer pregunta tiene una respuesta sorprendente: los paquetes, como los módulos, pueden requerir inicialización.

# La inicialización de un módulo se realiza mediante un código independiente (que no forma parte de ninguna función) ubicado dentro del archivo del módulo. Como un paquete no es un archivo, esta técnica es inútil para inicializar paquetes.

# En su lugar, debes usar un truco diferente: Python espera que haya un archivo con un nombre muy exclusivo dentro de la carpeta del paquete: __init__.py.

# El contenido del archivo se ejecuta cuando se importa cualquiera de los módulos del paquete. Si no deseas ninguna inicialización especial, puedes dejar el archivo vacío, pero no debes omitirlo.