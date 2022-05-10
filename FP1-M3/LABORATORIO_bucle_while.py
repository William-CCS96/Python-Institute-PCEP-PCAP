#Escenario
# Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

#Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

#La figura ilustra la regla utilizada por los constructores:


#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

#Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

#blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

#print("La altura de la pirámide:", height)

blocks=int(input("Cuantos bloques tines para la piramide: "))
height=1
addition_blocks=1

while True:
    if blocks==0:
        height=0
    if blocks<=2:
        break
    if blocks>=(addition_blocks+height):
       addition_blocks=addition_blocks+height+1
       height+=1
    if blocks<=(addition_blocks+height):
        break
print("La altura de la pirámide es:", height)


#bloques = int(input("Ingrese el número de bloques:"))
#altura=0
#while bloques-(altura+1)>=0: #Aumenta un nivel mientras los bloques alcance.
    #bloques-=(altura+1)
    #altura+=1;
 
#print("La altura de la pirámide:", altura)

