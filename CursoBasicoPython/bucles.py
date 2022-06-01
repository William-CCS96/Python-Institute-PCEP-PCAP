from re import X



def run():
    x=2
    while True:
        b=2**x
        if b>=1000:
            print("Final")
            break
        else:
            print(b)
            x+=1

