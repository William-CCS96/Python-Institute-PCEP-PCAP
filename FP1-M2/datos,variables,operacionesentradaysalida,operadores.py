#Cómo escribir y ejecutar programas simples en Python.
#Qué son los literales, operadores y expresiones en Python.
#Qué son las variables y cuáles son las reglas que las gobiernan.
#Cómo realizar operaciones básicas de entrada y salida.

from cmath import e


print("¡Hola Mundo!")

print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

print("La Witsi Witsi Araña subió a su telaraña.")
print()    
print("Vino la lluvia y se la llevó.")

#La barra invertida (\) tiene un significado muy especial cu,o se usa dentro de las cadenas, es llamado el carácter de escape.
#La palabra escape debe entenderse claramente: significa que la serie de caracteres en la cadena se escapa (detiene) por un momento (un momento muy corto) para introducir una inclusión especial.
#En otras palabras, la barra invertida no significa nada, sino que es solo un tipo de anuncio, de que el siguiente carácter después de la barra invertida también tiene un significado diferente.
#La letra n colocada después de la barra invertida proviene de la palabra newline (nueva línea).


print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()    
print("Vino la lluvia\ny se la llevó.")

print("\\")
print("Vino la lluvia\ry se la llevó.")
print("Quien soy\rno lo se.")

print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")
print("La Witsi Witsi Araña" , "\nsubió" , "\na su telaraña.")

#ARGUMENTO DE PALABRA CLAVE

#end
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

print("Mi nombre es ", end="")
print("Monty Python.")
x, y = 1, 2
print(x, y, end = "*")

#sep
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
#>Mi-nombre-es-Monty-Python.
print("Mi", "nombre", "es", "Monty", "Python.", sep="")
#>MinombreesMontyPython.

#sep y end
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#LABORATORIO: La función print()
#Salida esperada: Fundamentos***Programación***en...Python
#print("Fundamentos","Programación","en")
#print("Python")

print("Fundamentos","Programación","en", sep="***", end="...")
print("Python")
print("Fundamentos","Programación","en",sep="-",end="..Final ")
print("Python")

#LABORATORIO: D,o formato a la salida
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****",sep="\n")


print("    *"," ","   * *"," ","  *   *"," "," *     *"," ","***   ***"," ","  *   *"," ","  *   *"," ","  *****",sep="\n")

print("    *    "*2,"   * *   "*2,"  *   *  "*2," *     * "*2,"***   ***"*2,"  *   *  "*2,"  *   *  "*2,"  *****  "*2,sep="\n")



a=" "
b="  "
c="   "
d="    "
e="     "
f="    *"
g="   * *"
h="  *   *"
i=" *     *"
j="*     "
k="******"

print(d,f,c,e,"\n",d,g,b,e,"\n",d,h,b,d,"\n",d,i,e,"\n",f,c,f,d,"\n",c,j,f,c,"\n",b,j,b,f,b,"\n",a,j,c,a,f,a,"\n",k,e,k,"\n",e,j,j,"\n",e,j,j,"\n",e,j,j,"\n",e,j,j,"\n",e,k,j, sep="")

print(d,f,c,e,d,f,c,e,"\n",d,g,b,e,d,g,b,e,"\n",d,h,b,d,d,h,b,d,"\n",d,i,e,d,i,e,"\n",f,c,f,d,f,c,f,d,"\n",c,j,f,c,c,j,f,c,"\n",b,j,b,f,b,b,j,b,f,b,"\n",a,j,c,a,f,a,a,j,c,a,f,a,"\n",k,e,k,k,e,k,"\n",e,j,j,e,j,j,"\n",e,j,j,e,j,j,"\n",e,j,j,e,j,j,"\n",e,j,j,e,j,j,"\n",e,k,j,e,k,j, sep="")

