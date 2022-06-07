def is_prime(num):
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

print(is_prime(2781))

b=0
while True:
    if b>1000000:
        break
    if is_prime(b)==True:
        print(b)
        b+=1
    else:
        b+=1
        
        

        
#  is_prime(i + 1):
# 			print(i + 1, end=" ")
# print()
