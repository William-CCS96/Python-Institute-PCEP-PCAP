"""¿Cómo saber dónde estás?"""

# A veces, puede ser necesario encontrar información no relacionada con Python. Por ejemplo, es posible que necesites conocer la ubicación de tu programa dentro del entorno de la computadora.

# Imagina el entorno de tu programa como una pirámide que consta de varias capas o plataformas.

# Capas del entorno del programa

# Las capas son:

            # El código (en ejecución) se encuentra en la parte superior.
            # Python (mejor dicho, su entorno de ejecución) se encuentra directamente debajo de él.
            # La siguiente capa de la pirámide se llena con el SO (sistema operativo): el entorno de Python proporciona algunas de sus funcionalidades utilizando los servicios del sistema operativo. Python, aunque es muy potente, no es omnipotente: se ve obligado a usar muchos ayudantes si va a procesar archivos o comunicarse con dispositivos físicos.
            # La capa más inferior es el hardware: el procesador (o procesadores), las interfaces de red, los dispositivos de interfaz humana (ratones, teclados, etc.) y toda otra maquinaria necesaria para hacer funcionar la computadora: el sistema operativo sabe como emplearlos y utiliza muchos trucos para trabajar con todas las partes en un ritmo constante.

# Esto significa que algunas de las acciones del programa tienen que recorrer un largo camino para ejecutarse con éxito, imagina que:

            # Tu código quiere crear un archivo, por lo que invoca una de las funciones de Python.
            # Python acepta la orden, la reorganiza para cumplir con los requisitos del sistema operativo local, es como poner el sello "aprobado" en una solicitud y lo envía (esto puede recordarte una cadena de mando).
            # El SO comprueba si la solicitud es razonable y válida (por ejemplo, si el nombre del archivo se ajusta a algunas reglas de sintaxis) e intenta crear el archivo. Tal operación, aparentemente es muy simple, no es atómica: consiste de muchos pasos menores tomados por:
            # El hardware, el cual es responsable de activar los dispositivos de almacenamiento (disco duro, dispositivos de estado sólido, etc.) para satisfacer las necesidades del sistema operativo.
            
# Por lo general, no eres consciente de todo ese alboroto: quieres que se cree el archivo y eso es todo.

# Pero a veces quieres saber más, por ejemplo, el nombre del sistema operativo que aloja Python y algunas características que describen el hardware que aloja el sistema operativo.

# Hay un módulo que proporciona algunos medios para permitir saber dónde se encuentra y qué componentes funcionan. El módulo se llama platform. Veamos algunas de las funciones que brinda para ti.