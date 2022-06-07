# Ejercicio 5.7.1. Escribir un programa que reciba una a una las notas del usuario, preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

# def average_note()

qualification=[] 

def correct():  
    note=float(input("""
    Indicate your grade to know your grade point average
    """))
    while note<0.0 or note>5.0:
        print("Indica un valor valido")
        note=float(input("""
        Indicate your grade to know your grade point average
        """))
    qualification.append(note)   

def average():
    average_result=0
    for i in qualification:
        average_result+=i
    print("El promedio de tus notas es de:",round(average_result/len(qualification),2))
    print("Llevas",len(qualification), "calificaciones")

def answer():
    global question
    question=int(input("""
    ¿Deseas introducir más notas, indica 1 ó 2: 
    1. Si
    2. No
    """))
    while question<1 or question>2:
        print("Indica un valor valido")
        question=int(input("""
        ¿Deseas introducir más notas, indica 1 ó 2: 
        1. Si
        2. No
        """))
    
while True:
    correct()
    if len(qualification)==1:
        print("Tu promedio es de:", qualification[0])
        print("Llevas",len(qualification), "calificación")
    elif len(qualification)>1:
        average()
    answer()
    if question==1:
        continue
    elif question==2:
        break 
            

    
        




    