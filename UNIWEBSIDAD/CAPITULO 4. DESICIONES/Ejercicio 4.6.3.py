# Ejercicio 4.6.3. Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.

def identidad(n):
	MI = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
	return MI

print (identidad(3))

n = int(input('Introduce un entero positivo: '))
 
M = [] # Matriz
for i in range(n):
	fila = []
	for j in range(n):
		val = 1 if i==j else 0
		fila.append(val)
	M.append(fila)
 
print(M)