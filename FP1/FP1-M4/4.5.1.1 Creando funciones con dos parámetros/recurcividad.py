# Aquí, la recursividad es una técnica donde una función se invoca a si misma.

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
    # 1 -> 1
    # 2 -> 1
    # 3 -> 2
    # 4 -> 3
    # 5 -> 5
    # 6 -> 8
    # 7 -> 13
    # 8 -> 21
    # 9 -> 34

# la función fib() con recursividad
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))

# El factorial también tiene un lado recursivo. Observa:
    # n! = 1 × 2 × 3 × ... × n-1 × n
# Es obvio que:
    # 1 × 2 × 3 × ... × n-1 = (n-1)!
# Entonces, finalmente, el resultado es:
    # n! = (n-1)! × n

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

print(factorial_function(4))
    #24