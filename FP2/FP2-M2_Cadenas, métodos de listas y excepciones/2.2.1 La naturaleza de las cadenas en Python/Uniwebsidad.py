from itertools import count


print("\"Un divertido "+"programa "+"de radio.\"")
print("Hola, "+"hola, "*4+"tú")
a="Hola mundo mundano"
print(len(a))
b=""
print(len(b))
for letter in a:
    print(letter,end=" ")
print()
print(a[-1])
# Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres de una cadena del final al principio.
for letter in range(len(a)):
    print(a[(letter+1)*-1],end="")

print(a[1:])
print(a[5:10])
print(a[0:0])

# Problema 6.1. Nuestro primer problema es muy simple: Queremos contar cuántas letras A hay en una cadena x.
x="akgufmAjdlalmfjAjufiA"
print(x.count("A"))

def count_letter(string,character):
    count=0
    for letter in string:
        if character==letter:
            count+=1
    print(count)   

count_letter(x,"u")
ti="jfhf68snf26snfjdm11"
count_letter(ti,"2")

# Ejercicio 6.5. ¿Hay más letras A o más letras E en una cadena? Escribir un programa que lo decida.
def comp_char(string,x,y):
    countx=string.count(x)
    county=string.count(y)
    if countx==county:  print("Equal amount entre character",x,"and",y)
    elif county>countx: print("There are more characters",y)
    else: print("There are more characters",x)

comp_char(ti,"1","6")

# Ejercicio 6.6. Escribir un programa que cuente cúantas veces aparecen cada una de las vocales en una cadena. No importa si la vocal aparece en mayúscula o en minúscula.
ti="igodhdurteial857o"
def count_vowels(string):
    vowels="aeiou"
    string_lower=string.lower()
    a=0
    e=0
    i=0
    o=0
    u=0    
    for char in string_lower:
        if char in vowels:
            if char=="a":a+=1
            elif char=="e":e+=1
            elif char=="i":i+=1
            elif char=="o":o+=1
            elif char=="u":u+=1
    print("The string "+"("+string+")"+" there are this number of vowels:"+"\na="+str(a)+", "+"e="+str(e)+", "+"i="+str(i)+", "+"o="+str(o)+", "+"u="+str(u)+".")

count_vowels(x)
    
