
def divisores(num):
    num_divisores=[]
    x=1
    while True:
        if num==x:
            break
        if num%x==0:
            num_divisores.append(x)
        x+=1
    return num_divisores

perfect=0
for i in divisores(6):
    perfect+=i
print(perfect)
print(divisores(6))

