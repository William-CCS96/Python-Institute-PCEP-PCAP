#"=" es un simbolo para designar un valor
# "==" compara los dos valores a==b, pregunta

    #Pregunta1
2==2
    #true

    #Ahora imagina a un programador que sufre de insomnio, y tiene que contar las ovejas negras y blancas por separado siempre y cuando haya exactamente el doble de ovejas negras que de las blancas.
    #black_sheep == (2 * white_sheep)

var = 0   # asignando 0 a var
print(var == 0)
    #True

var = 1  # asignando 1 a var
print(var == 0)
    #False


#DESAIGUALDAD: el operadore no es igual a (!=)
var = 0 # asignando 0 a var
print(var != 0)
    #False
var = 1 # asignando 1 a var
print(var != 0)
    #True

#OPERADORES DE COMPARACIÓN:   MAYOR QUE
    #black_sheep > white_sheep  # mayor que

#OPERADORES DE COMPARACIÓN:     MAYOR O IGUAL QUE
    #operadores binarios con enlace del lado izquierdo

#OPERADORES DE COMPARACIÓN:     MENOR O IGUAL QUE
    #current_velocity_mph < 85  # Menor que
    #current_velocity_mph <= 85  # Menor o igual que


    #QUE SE HACE CON LAS RESPUESTAS DE KIS COMPARADORES
        #Almacenarlo como una variables
            #answer = number_of_lions >= number_of_lionesses
        #Puedes utilizar la respuesta que obtengas para tomar una decisión sobre el futuro del programa.


            # Prioridad	Operador	
                # 1	+, -	    unario
                # 2	**	
                # 3	*, /, //, %	
                # 4	+, -	    binario
                # 5	<, <=, >, >=	
                # 6	==, !=

#LABORATORIO
#Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True si n es mayor o igual que 100.


n=int(input("Escribe tu numero n"))
print(str(n) + " es mayor que 100: "+ str((n>100))+".")
    # 102 es mayor que 100: True





