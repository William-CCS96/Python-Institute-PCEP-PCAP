# Pruebas y probadores
# La respuesta es más simple de lo esperado y también un poco decepcionante. Python, como seguramente sabes, es un lenguaje interpretado. Esto significa que el código fuente se analiza y ejecuta al mismo tiempo. En consecuencia, es posible que Python no tenga tiempo para analizar las líneas de código que no están sujetas a ejecución. Como dice un antiguo dicho de los desarrolladores: "es una característica, no un error" (no utilices esta frase para justificar el comportamiento extraño de tu código).

# ¿Entiendes ahora por qué el pasar por todos los caminos de ejecución es tan vital e inevitable?

# Supongamos que terminas tu código y que las pruebas que has realizado son exitosas. Entregas tu código a los probadores y, ¡afortunadamente! - encontraron algunos errores en él. Estamos usando la palabra "afortunadamente" de manera completamente consciente. Debes aceptar que, en primer lugar, los probadores son los mejores amigos del desarrollador; no debes tratar a los errores que ellos encuentran como una ofensa o una malignidad; y, en segundo lugar, cada error que encuentran los probadores es un error que no afectará a los usuarios. Ambos factores son valiosos y merecen tu atención.

# Ya sabes que tu código contiene un error o errores (lo segundo es más probable). Ahora, ¿cómo los localizas y cómo arreglas tu código?

# Error frente a depuración (Bug vs. debug)

# La medida básica que un desarrollador puede utilizar contra los errores es, como era de esperarse, un depurador, mientras que el proceso durante el cual se eliminan los errores del código se llama depuración. Según un viejo chiste, la depuración es un complicado juego de misterio en el que eres simultáneamente el asesino, el detective y, la parte más dolorosa de la intriga, la víctima. ¿Estás listo para interpretar todos estos roles? Entonces debes armarte con un depurador.

# Un depurador es un software especializado que puede controlar cómo se ejecuta tu programa. Con el depurador, puedes ejecutar tu código línea por línea, inspeccionar todos los estados de las variables y cambiar sus valores en cualquier momento sin modificar el código fuente, detener la ejecución del programa cuando se cumplen o no ciertas condiciones, y hacer muchas otras tareas útiles.

# Podemos decir que todo IDE está equipado con un depurador más o menos avanzado. Incluso IDLE tiene uno, aunque puedes encontrar su manejo un poco complicado y problemático. Si deseas utilizar el depurador integrado de IDLE, debes activarlo mediante la opción "Debug" en la barra de menú de la ventana principal de IDLE. Es el punto de partida para la depuración.

# Las capturas de pantalla que ves al lado muestran el depurador IDLE durante una simple sesión de depuración.

# Puedes ver cómo el depurador visualiza las variables y los valores de los parámetros. Observa la pila de llamadas que muestra la cadena de invocaciones que van desde la función actualmente ejecutada hacia el intérprete.

# Si deseas saber más sobre el depurador IDLE, consulta la documentación IDLE.

    
    #utilizar depugging desde la shell de pyhton:
    # https://www.cs.uky.edu/~keen/help/debug-tutorial/debug.html