
# . Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.


def review_examen():
    name=input("Ingresa el nombre del alumno ó 1 para salir: ")
    while name!="1":
        while True:
            try:
                points=int(input("Indica la cantidad de ejercicios resultos por el alumno: "))
            except:
                print("Ingresa un número entre 0 y 10")
                continue
            if points<0 or points>10:
                continue
            else:
                break
        print("El alumno", name,"resolvio el", points*10,"%","del examen")
        if points<6:
            print("El alumno:","Reprobo.")
        else:
            print("El alumno:","Aprobo.")
        name=input("Ingresa el nombre del alumno ó 1 para salir: ")
    else:
        print("¡Gracias!")
review_examen()

# Ingresa el nombre del alumno ó 1 para salir: Luis
# Indica la cantidad de ejercicios resultos por el alumno-
# Ingresa un número entre 0 y 10
# Indica la cantidad de ejercicios resultos por el alumno/
# Ingresa un número entre 0 y 10
# Indica la cantidad de ejercicios resultos por el alumno*
# Ingresa un número entre 0 y 10
# Indica la cantidad de ejercicios resultos por el alumno-5
# Indica la cantidad de ejercicios resultos por el alumno6
# El alumno Luis resolvio el 60 % del examen
# El alumno: Aprobo.
# Ingresa el nombre del alumno ó 1 para salir: 1
# ¡Gracias!