# Ejercicio 5.7.10. Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.


def num_prime(num):
    x=2
    while True:
        if num==1:
            return False
        if num==x:
            return True  
        if num%x!=0:
            x+=1
        else:
            return False

def primos_num(a):
    primes=[]
    num=2
    if a<num:
        return print("El número indicado no puede ser menor que 2")
    while True:
        if num>a:
            break
        if num_prime(num)==True:
            primes.append(num)
            num+=1
        else:
            num+=1
    return primes
    
print(primos_num(45))
    
        
            

