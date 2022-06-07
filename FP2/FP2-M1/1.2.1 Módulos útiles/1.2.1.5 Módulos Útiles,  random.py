# ¿Existe aleatoriedad real en las computadoras?
# Otro módulo que vale la pena mencionar es el que se llama random.

# Ofrece algunos mecanismos que permiten operar con números pseudoaleatorios.

# Dos dados â el concepto de aleatoriedad
# Toma en cuenta el prefijo pseudo - los números generados por los módulos pueden parecer aleatorios en el sentido de que no se pueden predecir, pero no hay que olvidar que todos se calculan utilizando algoritmos muy refinados.

# Los algoritmos no son aleatorios, son deterministas y predecibles. Solo aquellos procesos físicos que se salgan completamente de nuestro control (como la intensidad de la radiación cósmica) pueden usarse como fuente de datos aleatorios reales. Los datos producidos por computadoras deterministas no pueden ser aleatorios de ninguna manera.

# Un generador de números aleatorios toma un valor llamado semilla, lo trata como un valor de entrada, calcula un número "aleatorio" basado en él (el método depende de un algoritmo elegido) y produce una nueva semilla.

# La duración de un ciclo en el que todos los valores semilla son únicos puede ser muy largo, pero no es infinito: tarde o temprano los valores iniciales comenzarán a repetirse y los valores generadores también se repetirán. Esto es normal. Es una característica, no un error.

# El valor de la semilla inicial, establecido durante el inicio del programa, determina el orden en que aparecerán los valores generados.

# El factor aleatorio del proceso puede ser aumentado al establecer la semilla tomando un número de la hora actual - esto puede garantizar que cada ejecución del programa comience desde un valor semilla diferente (por lo tanto, usará diferentes números aleatorios).

# Afortunadamente, Python realiza dicha inicialización al importar el módulo.

