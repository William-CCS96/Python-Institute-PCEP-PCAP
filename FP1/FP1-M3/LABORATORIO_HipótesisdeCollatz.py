#Escenario
#En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

#1. Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
#2. Si es par, evalúa un nuevo c0 como c0 Ã· 2.
#3. De lo contrario, si es impar, evalúe un nuevo  c0  como 3 Ã c0 + 1.
#4. Si c0 â  1, salta al punto 2.
#La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

#Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.

#Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.

#Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito.

cO=int(input("Introduce tu número a probar: "))
pasos=0

while cO!=1:
    if cO%2==0:
        cO=int(cO/2)
        print(cO)
        pasos+=1
    else:
        cO=int((cO*3)+1)
        print(cO)
        pasos+=1

print("pasos: ",pasos)

    