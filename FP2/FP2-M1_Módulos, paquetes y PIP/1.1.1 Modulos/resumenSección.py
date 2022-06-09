# Puntos Claves

# 1. Si deseas importar un módulo como un todo, puedes hacerlo usando la sentencia import nombre_del_módulo. Puedes importar más de un módulo a la vez utilizando una lista separada por comas. Por ejemplo:

import mod1
import mod2, mod3, mod4


# Aunque la última forma no se recomienda por razones estilísticas, y es mejor y más bonito expresar la misma intención de una forma más detallada y explícita, como por ejemplo:

import mod2
import mod3
import mod4


# 2. Si un módulo se importa de la manera anterior y desea acceder a cualquiera de sus entidades, debes anteponer el nombre de la entidad empleando la notación con punto. Por ejemplo:

import my_module

result = my_module.my_function(my_module.my_data)

# El fragmento de código utiliza dos entidades que provienen del módulo my_module: una función llamada my_function() y una variable con el nombre my_data. Ambos nombres deben tener el prefijo my_module. Ninguno de los nombres de entidad importados entra en conflicto con los nombres idénticos existentes en el namespace de tu código.


# 3. Se te permite no solo importar un módulo como un todo, sino también importar solo entidades individuales de él. En este caso, las entidades importadas no deben especificar el prefijo cuando son empleadas. Por ejemplo:

from module import my_function, my_data

result = my_function(my_data)

# La forma anterior, a pesar de su atractivo, no se recomienda debido al peligro de causar conflictos con los nombres derivados de la importación del namespace del código.


# 4. La forma más general de la sentencia anterior te permite importar todas las entidades ofrecidas por un módulo:

from my_module import *

result = my_function(my_data)


# Nota: la variante de esta importación no se recomienda debido a las mismas razones que antes (la amenaza de un conflicto de nombres es aún más peligrosa aquí).

# 5. Puede cambiar el nombre de la entidad importada "sobre la marcha" utilizando la frase as del import. Por ejemplo:

from module import my_function as fun, my_data as dat

result = fun(dat)


#-------------------------
# Ejercicio 1
# Quieres invocar la función make_money() contenida en el módulo llamado mint. Tu código comienza con la siguiente línea:
import mint

# ¿Cuál es la forma adecuada de invocar a la función?
mint.make_money()


# Ejercicio 2
# Quieres invocar la función make_money() contenida en el módulo llamado mint. Tu código comienza con la siguiente línea:
from mint import make_money
	
# ¿Cuál es la forma adecuada de invocar a la función?
make_money()



# Ejercicio 3
# Has escrito una función llamada make_money por tu cuenta. Necesitas importar una función con el mismo nombre del módulo mint y no deseas cambiar el nombre de ninguno de tus nombres previamente definidos. ¿Qué variante de la sentencia import puede ayudarte con el problema?

from mint import make_money as make_more_money


# Ejercicio 4
# ¿Qué forma de invocación de la función make_money es válida si tu código comienza con la siguiente línea?
from mint import *

make_money()