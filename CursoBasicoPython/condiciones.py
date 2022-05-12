edad=int(input("¿Qué edad tienes?: "))
0
if edad>=18:
    if edad>=18 and edad<100:
        print("Eres mayor de edad")
    else:
        print("Eres un fantasma")
else:
    if edad<18 and edad>=0:
        print("Eres menor de edad")
    else:
        print("No has nacido")
        edad=int(input("¿Qué edad tienes?: "))
