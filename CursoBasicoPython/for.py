def tabla_mul():
    num=int(input("Que tabla quieres ver: "))
    for i in range(1,11):
        print(str(num)+" x "+str(i)+": "+str(num*i))

if __name__=="__main__":
    tabla_mul()