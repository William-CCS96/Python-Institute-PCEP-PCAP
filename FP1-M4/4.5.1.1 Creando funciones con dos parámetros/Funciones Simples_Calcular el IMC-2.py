# Ahora trabajaremos con triángulos. Comenzaremos con una función que verifique si tres lados de ciertas longitudes pueden formar un triángulo.

# En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.

# No será algo difícil. La función tendrá tres parámetros - uno para cada lado.

# Regresará True si todos los lados pueden formar un triángulo, y False de lo contrario. En este caso, is_a_triangle es un buen nombre para dicha función.

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
    # True
    # False

#MAS COMPACTA:
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

#AÚN MÁS  COMPACTA
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

    # Se ha negado la condición (se invirtieron los operadores relacionales y se reemplazaron los ors con ands, obteniendo una expresión universal para probar triángulos).

    # Coloquemos la función en un programa más grande. Se le pedirá al usuario los tres valores y se hará uso de la función.

#----------------------------------
# Algunas funciones simples: triángulos y el Teorema de Pitágoras
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')

# En el segundo paso, intentaremos verificar si un triángulo es un triángulo rectángulo.
# Para ello haremos uso del Teorema de Pitágoras:
# c2 = a2 + b2

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2 #Se agrego la validación con el cateto b
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(is_a_right_triangle(3, 5, 4))
print(is_a_right_triangle(9, 5, 7))

#------------------------------
# Algunas funciones simples: evaluando el área de un triángulo
    #También es posible evaluar el área de un triángulo. La Formula de Heron será útil aquí:

    # s = (a+b+c)/2
    # A= raiz(s(s-a)*(s-b)*(s-c))
    # raiz(x) = x **0.5

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))
    # 0.49999999999999983
    #  Lo probaremos con un triángulo rectángulo la mitad de un cuadrado y con un lado igual a 1. Esto significa que su área debe ser igual a 0.5.
    