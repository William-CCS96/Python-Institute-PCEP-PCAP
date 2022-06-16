# Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.

# Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).

# Usando la primera función, escribir una función que imprima las primeras m parejas de números (a,b), tales que la suma de los divisores de a es igual a b y la suma de los divisores de b es igual a a (es decir las primeras m parejas de números amigos).

# Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.

"""Divisores de un número natural"""
def divisores(num):
    num_divisores=[]
    x=1
    while True:
        if num==1:
            num_divisores=[1]
            break
        if num==x:
            break
        if num%x==0:
            num_divisores.append(x)
        x+=1
    return num_divisores

print(divisores(2456))

"""Los primeros m números perfectos"""
def num_perfect(m):
    x=1
    list_perfect=[]
    count=0
    while True:
        if count==m:
            break
        if (x%3==0 or x%5==0)and(x!=6 and x!=3):
            x+=1
            continue
        if len(divisores(x))==1:
            x+=1
            continue
        perfect=0
        for i in divisores(x):
            perfect+=i
        if perfect==x:
            list_perfect.append(x)
            count+=1
            perfect=0
            x+=1
        else:
            x+=1
    print(list_perfect) 

num_perfect(2)


"""Las primeras x parejas número amigos"""
def nums_friends(x):
    friends=[]
    count=0
    num1=4
    while True:
        if count==x:
            break
        adding_num1=0
        adding_num2=0
        if num1 in friends:
            num1+=1
            continue 
        if len(divisores(num1))==1:
            num1+=1
            continue 
        for i in divisores(num1):
            adding_num1+=i
        if adding_num1==num1:
            num1+=1
            continue 
        if len(divisores(adding_num1))==1:
            num1+=1
            continue
        for i in divisores(adding_num1):
            adding_num2+=i
        if num1==adding_num2:
            friends.append(num1)
            friends.append(adding_num1)
            friends.append("-")
            count+=1
            num1+=1
        else:
            num1+=1
    return friends

print(nums_friends(2))







