#FACTORIALES

# 0! = 1 (¡Si!, es verdad.)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 ** 3 * 4 * ... * n-1 * n

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # probando
    print(n, factorial_function(n))
    # 1 1
    # 2 2
    # 3 6
    # 4 24
    # 5 120


#Formula para números factorialescon recursividad:
def factorial_recursividad(n):
    if n==0:
        return 1
    return factorial_recursividad(n-1)*n
  


