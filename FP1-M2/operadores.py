print(2+2)

    #Operadores Python relacionados con la aritmética
    #+, -, *, /, //, %, **
    #Recuerda: Cuando los datos y operadores se unen, forman juntos expresiones. La expresión más sencilla es el literal.

#EXPONENCIACIÓN
    # "**" :potencia
print(2**3)
#>8
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
    #8
    # 8.0
    # 8.0
    # 8.0

#MULTIPLICACIÓN
    #"*"
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
    # 6
    # 6.0
    # 6.0
    # 6.0

#DIVISIÓN
    #"/"
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
    # 2.0
    # 2.0
    # 2.0
    # 2.0
    #El resultado producido por el operador de división siempre es flotante

#DIVISIÓN ENTERA
    #"//"
    #los resultados siempre son redondeados.
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
    # 2
    # 2.0
    # 2.0
    # 2.0
print(6 // 4)
print(6. // 4)
    # 1
    # 1.0
        #El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada.
print(-6 // 4)
print(2. // -4)
    # -2
    # -2.0
    #La division entera también se le suele llamar en inglés floor division. Más adelante te cruzarás con este término.


#RESIDUO (MÓDULO)
    #"%"
    #El resultado de la operación es el residuo que queda de la división entera.
print(14 % 4)
    # 2
print(12 % 4.5)
    # 3.0
print(23 % 25) 
print(4002%4)

#DIVISIÓN ENTRE CERO NO FUNCIO
    #print(14 % 0)>ERROR

#SUMA
    #"+"
print(-4 + 4)
print(-4. + 8)
    # 0
    # 4.0

#RESTA (OPERADORES UNITARIOS Y BINARIOS)
    #"-"
    #Es un operador Binario
print(-4 -4)
print(4. -8)
print(-1.1)
    #-8
    # -4.0
    # -1.1
    #Operador + unitario
print(+5)
    #5


#PROPIEDADES OPERADORES
    #La multiplicación precede a la suma
    #Jerarquía de propiedades

#OPERADORESY SUS ENLACES
    #el cálculo de la expresión es realizado de izquierda a derecha.
print(9 % 6 % 2)
    # 1

    #Exponenciación
print(2 ** 2 ** 3)
    # 256
    #2**3 =8; 2**8 = 256    
    #l operador de exponenciación utiliza enlazado del lado derecho.

#LISTA DE PRIORIDADES
    #Prioridad	Operador	
        # 1	+, -	unario
        # 2	**	
        # 3	*, /, //, %	
        # 4	+, -	binario
print(2 * 3 % 5)
    # 1

#OPERADORES Y PARENTESIS
    #las sub-expresiones dentro de los paréntesis siempre se calculan primero.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
    # 10.0

#RESUMEN DE LA SECCIÓN
print((2 ** 4), (2 * 4.), (2 * 4))
    # 16 8.0 8
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
    #-0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
    #-2 2 512
    
20.12*10**8


