"""Enfoque procedimental frente al enfoque orientado a objetos"""
# En el enfoque procedimental, es posible distinguir dos mundos diferentes y completamente separados: el mundo de los datos y el mundo del código. El mundo de los datos está poblado con variables de diferentes tipos, mientras que el mundo del código está habitado por códigos agrupados en módulos y funciones.

# Las funciones pueden usar datos, pero no al revés. Además, las funciones pueden abusar de los datos, es decir, usar el valor de manera no autorizada (por ejemplo, cuando la función seno recibe el saldo de una cuenta bancaria como parámetro).

# Los datos no pueden usar funciones. ¿Pero es esto completamente cierto? ¿Hay algunos tipos especiales de datos que puedan usar funciones?

# Sí, los hay, los llamados métodos. Estas son funciones que se invocan desde dentro de los datos, no junto con ellos. Si puedes ver esta distinción, has dado el primer paso en la programación de objetos.

# El enfoque orientado a objetos sugiere una forma de pensar completamente diferente. Los datos y el código están encapsulados juntos en el mismo mundo, divididos en clases.

# Cada clase es como una receta que se puede usar cuando quieres crear un objeto útil. Puedes producir tantos objetos como necesites para resolver tu problema.

# Cada objeto tiene un conjunto de rasgos (se denominan propiedades o atributos; usaremos ambas palabras como sinónimos) y es capaz de realizar un conjunto de actividades (que se denominan métodos).

# Las recetas pueden modificarse si son inadecuadas para fines específicos y, en efecto, pueden crearse nuevas clases. Estas nuevas clases heredan propiedades y métodos de los originales, y generalmente agregan algunos nuevos, creando nuevas herramientas más específicas.

# Los objetos son encarnaciones de las ideas expresadas en clases, como un pastel de queso en tu plato, es una encarnación de la idea expresada en una receta impresa en un viejo libro de cocina.

# Los objetos interactúan entre sí, intercambian datos o activan sus métodos. Una clase construida adecuadamente (y, por lo tanto, sus objetos) puede proteger los datos sensibles y ocultarlos de modificaciones no autorizadas.

# No existe un límite claro entre los datos y el código: viven como uno solo dentro de los objetos.

# Todos estos conceptos no son tan abstractos como pudieras pensar al principio. Por el contrario, todos están tomados de experiencias de la vida real y, por lo tanto, son extremadamente útiles en la programación de computadoras: no crean vida artificial reflejan hechos reales, relaciones y circunstancias.