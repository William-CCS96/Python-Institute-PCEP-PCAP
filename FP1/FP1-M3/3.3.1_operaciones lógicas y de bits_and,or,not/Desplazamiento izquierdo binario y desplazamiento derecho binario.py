# La computadora realiza el mismo tipo de operación, pero con una diferencia: como dos es la base para los números binarios (no 10), desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos; respectivamente, desplazar un bit a la derecha es como dividir entre dos (observe que se pierde el bit más a la derecha).

# Los operadores de cambio en Python son un par de dígrafos: < < y > >, sugiriendo claramente en qué dirección actuará el cambio.


var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
#17 68 8

# Nota:

# 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)


# Prioridad	Operador	
# 1     	~, +, - 	unario
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	    binario
# 5	        <<, >>	
# 6	        <, <=, >, >=	
# 7	        ==, !=	
# 8	        &	
# 9	        |	
# 10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # !difícil!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)