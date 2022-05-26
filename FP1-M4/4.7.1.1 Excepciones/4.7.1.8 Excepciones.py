"""# Por qué no se puede evitar el probar tu código"""
# Aunque vamos a resumir nuestras consideraciones excepcionales aquí, no creas que es todo lo que Python puede ofrecer para ayudarte a suplicar perdón. La maquinaria de excepciones de Python es mucho más compleja y sus capacidades te permiten desarrollar estrategias de manejo de errores expandidas. Volveremos a estos temas, lo prometemos. No dudes en realizar tus experimentos y sumergirte en las excepciones por ti mismo.

# Ahora queremos contarte sobre el segundo lado de la lucha interminable contra los errores: el destino inevitable de la vida de un desarrollador. Como no puedes evitar la creación de errores en tu código, siempre debes estar listo para buscarlos y destruirlos. No entierres la cabeza en la arena: ignorar los errores no los hará desaparecer.

# Un deber importante para los desarrolladores es probar el código recién creado, pero no debes olvidar que las pruebas no son una forma de demostrar que el código está libre de errores. Paradójicamente, lo único que las pruebas determinan, es que tu código contiene errores. No creas que puedes relajarte después de una prueba exitosa.

# El segundo aspecto importante de las pruebas de software es estrictamente psicológico. Es una verdad conocida desde hace años que los autores, incluso aquellos que son confiables y conscientes de sí mismos, no pueden evaluar y verificar objetivamente sus trabajos.

# Es por eso por lo que cada novelista necesita un editor y cada programador necesita un "tester". Algunos dicen, con un poco de rencor, pero con sinceridad, que los desarrolladores prueban su código para mostrar su perfección, no para encontrar problemas que puedan frustrarlos. Los "testers" o probadores están libres de tales dilemas, y es por eso por lo que su trabajo es más efectivo y rentable.

# Por supuesto, esto no te exime de estar atento y cauteloso. Prueba tu código lo mejor que puedas. No facilites demasiado el trabajo a los probadores.

# Su deber principal es asegurarse de haber verificado todas las rutas o caminos de ejecución por las que puede pasar tu código. ¿Suena misterioso? ¡Por supuesto que no!

"""# Rastreando las rutas de ejecución"""
# Supón que acabas de terminar de escribir este fragmento de código.

# Existen tres rutas o caminos de ejecución independientes en el código, ¿puedes verlas? Están determinadas por las sentencias if-elif-else. Por supuesto, las rutas de ejecución pueden construirse mediante muchas otras sentencias como bucles, o incluso bloques try-except.
# Si vas a probar tu código de manera justa y quieres dormir profundamente y soñar sin pesadillas (las pesadillas sobre errores pueden ser devastadoras para el rendimiento de un desarrollador), estás obligado a preparar un conjunto de datos de prueba que obligará a tu código a negociar todos los posibles caminos.

# En nuestro ejemplo, el conjunto debe contener al menos tres valores flotantes: uno positivo, uno negativo y cero.
try:
    temperature = float(input('Ingresa la temperatura actual:'))
    if temperature > 0:
        print("Por encima de cero")
    elif temperature < 0:
        print("Por debajo de cero")
    else:
        print("Cero")
except:
    print("Error, introduce un número real")

