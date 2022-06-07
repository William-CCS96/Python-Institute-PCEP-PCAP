#poseen una prioridad inferior a la expresada por los operadores de comparación
#CONJUNCIÓN
    #and (y)
#DISYUNCIÓN
    #or (o)
#and
counter > 0 and value == 100

# Argumento A	Argumento B	A and B
# False	        False	     False
# False	        True	     False
# True       	False	     False
# True      	True	     True

#or
    #Con una prioridad más baja que and (al igual que + en comparación con *).}

# Argumento A	Argumento B	A and B
# False	        False	     False
# False	        True	     True
# True       	False	     True
# True      	True	     True

#not
    #Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad
    #su prioridad es muy alta: igual que el unario + y -

# Argumento    not Argumento
# False         True
# True          False



#EXPRESIONES LÓGICAS
#Son equivalentes:
# Ejemplo 1:  
var=1  
print(var > 0)  #True
print(not (var <= 0)) #True


# Ejemplo 2:
print(var != 0)  #True
print(not (var == 0)) #True


#leyes de De Morgan. Dicen que:
# La negación de una conjunción es la separación de las negaciones.
# La negación de una disyunción es la conjunción de las negaciones.

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

#OPERADORES bit a bit
    #Agreguemos un comentario importante: los argumentos de estos operadores deben ser enteros. No debemos usar flotantes aquí. 
    #Operadore xor
        #(Significa o exclusivo) y se denota como ^ (signo de intercalación).

    #  &  (ampersand) - conjunción a nivel de bits.
    #  |  (barra vertical) - disyunción a nivel de bits.
    #  ~  (tilde) - negación a nivel de bits.
    #  ^  (signo de intercalación) - o exclusivo a nivel de bits (xor)

    #Operaciones
    # Argumento A	Argumento B	    A & B	 A | B  	A ^ B
    # 0             	0	         0      	0	        0
    # 0	                1	         0         	1	        1
    # 1	                0            0      	1	        1
    # 1	                1	         1	        1	        0

    #Operaciones bit a bit ~ 
    # Argumento	    ~ Argumento
    #    0	            1
    #    1              0

    # & requieres exactamente dos 1s para proporcionar 1 como resultado.
    # | requiere al menos un 1 para proporcionar 1 como resultado.
    # ^ requiere exactamente un 1 para proporcionar 1 como resultado.

    #Se pueden utilizar de forma abreviada
    
    # x = x & y 	x &= y
    # x = x | y	    x |= y
    # x = x ^ y 	x ^= y


