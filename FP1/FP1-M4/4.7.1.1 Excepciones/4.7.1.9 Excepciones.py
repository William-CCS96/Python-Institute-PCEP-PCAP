"""
# Cuando Python cierra sus ojos"""
# Tal prueba es crucial. Queremos mostrarte por qué no debes omitirlo. Observa el siguiente código.

# Introdujimos intencionalmente un error en el código; esperamos que tus ojos atentos lo noten de inmediato. Sí, eliminamos solo una letra y, en efecto, la invocación válida de la función print() se convierte en la obviamente inválida invocación "prin()". No existe tal función como "prin()" en el alcance de nuestro programa, pero ¿es realmente obvio para Python?

# Ejecuta el código e ingresa un 0.

# Como puedes ver, el código finaliza su ejecución sin ningún obstáculo.

# ¿Cómo es eso posible? ¿Por qué Python pasa por alto un error de desarrollador tan evidente?

# ¿Puedes encontrar las respuestas a estas preguntas fundamentales?



temperature = float(input('Ingresa la temperatura actual:'))

if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    prin("Por debajo de cero")
else:
    print("Cero")
