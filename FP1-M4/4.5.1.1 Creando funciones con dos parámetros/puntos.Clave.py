# Puntos Clave
# 1. Una función puede invocar otras funciones o incluso a sí misma. Cuando una función se invoca a si misma, se le conoce como recursividad, y la función que se invoca a si misma y contiene una condición de terminación (la cual le dice a la función que ya no siga invocándose a si misma) es llamada una función recursiva.

# 2. Se pueden emplear funciones recursivas en Python para crear funciones limpias, elegantes, y dividir el código en trozos más pequeños. Sin embargo, se debe tener mucho cuidado ya que es muy fácil cometer un error y crear una función la cual nunca termine. También se debe considerar que las funciones recursivas consumen mucha memoria, y por lo tanto pueden ser en ocasiones ineficientes.

# Al emplear la recursividad, se deben de tomar en cuenta tanto sus ventajas como desventajas.

# La función factorial es un ejemplo clásico de como se puede implementar el concepto de recursividad:
# Implementación recursiva de la función factorial.

def factorial(n):
    if n == 1:    # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24

# Ejercicio 1
# ¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de código y por qué?
def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))
    # La función no tiene una condición de terminación, por lo tanto Python arrojara una excepción (RecursionError: maximum recursion depth exceeded)

# Ejercicio 2
# ¿Cuál es la salida del siguiente fragmento de código?
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
# 56