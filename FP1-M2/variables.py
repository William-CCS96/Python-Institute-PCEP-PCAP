#Palabras claves no usar como nombre de variables:
    #['False', 'None', 'True', ',', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    #No es necesario declararlas
    #La creación (o su sintaxis) es muy simple: solo utiliza el nombre de la variable deseada, después el signo de igual (=) y el valor que se desea colocar dentro de la variable.


var = 1
print(var)

var2 = 2
client_name= "Juanito"
account_balance= 1000.0
print(var2, client_name, account_balance, sep=", ")
    #>2, Juanito, 1000.0

#COMBINAR CADENAS CON VARIABLES "+"
let= "hermoxito"
let1= "Juanito "
print(let1+let)
    #Juanito hermoxito

#ASIGANR UN VALOR NUEVO A UNA VARIABLES
age_Juanito=19
print(age_Juanito)
age_Juanito= age_Juanito+1
print(age_Juanito)
#>20
var = 100
var = 200 + 300
print(var)
#>500

#RESOLVIENDO PROBLEMAS MATEMÁTICOS
    #TEOREMA DE PITAGORAS
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#LABORATORIO: VARIABLES
    #Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

    #Tu tarea es:

    #Crear las variables: juan, maria, y adan.
    # Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía.
    # Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
    # Después se debe crear una nueva variable llamada total_manzanas y se debe igualar a la suma de las tres variables anteriores.
    # Imprime el valor almacenado en total_manzanas en la consola.
    # Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número Total de Manzanas:" y total_manzanas.

juan_numer_manzanas= 3
maria_number_manzanas= 5
adan_numer_manzanas= 6
print(juan_numer_manzanas,maria_number_manzanas,adan_numer_manzanas, sep=", ")
total_manzanas=juan_numer_manzanas+maria_number_manzanas+adan_numer_manzanas
print(total_manzanas)
resta_juan_adan_manzanas=juan_numer_manzanas-adan_numer_manzanas
print(resta_juan_adan_manzanas)
multiplicacion_maria_adan_manzanas=maria_number_manzanas*adan_numer_manzanas
print(multiplicacion_maria_adan_manzanas)
division_maria_adan_manzanas=(maria_number_manzanas/adan_numer_manzanas)
print(division_maria_adan_manzanas)
division_entero_maria_juan_manzanas=(maria_number_manzanas//juan_numer_manzanas)
print(division_entero_maria_juan_manzanas)
modulo_maria_juan_manzanas=maria_number_manzanas%juan_numer_manzanas
print(modulo_maria_juan_manzanas)
exponencial_maria_juan_manzanas=maria_number_manzanas**juan_numer_manzanas
print(exponencial_maria_juan_manzanas)

#OPERADORES ABREVIADOS
    # x =x*2  igual a x *= 2
    # i = i + 2 * j ⇒ i += 2 * j
    # var = var / 2 ⇒ var /= 2
    # rem = rem % 10 ⇒ rem %= 10
    # j = j - (i + var + rem) ⇒ j -= (i + var + rem)
    # x = x ** 2 ⇒ x **= 2
age_Juanito=19
age_Juanito+= 5
print(age_Juanito)
#>24

#lABORATORIO, UN SENCILLO CONVERTIDOR
    #Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:
        # Millas a kilómetros.
        # Kilómetros a millas.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
        #round(variable, numerodedigitos) = redondea la cifra de la variable al numero dedigitos que deseemos
    
    # 7.38 millas son 11.88 kilómetros
    # 12.25 kilómetros son 7.61 millas

#CONVERTIDOR DE GRADOS CENTIGRADOS
grados_centigrados= 42
grados_kelvin= 345

grados_centigrados_to_grados_kelvin= grados_centigrados+273.15 
grados_kelvin_to_grados_centigrados=grados_kelvin-273.15 

print(grados_centigrados, "°C son", round(grados_centigrados_to_grados_kelvin, 1) , "°K" )
print(grados_kelvin, "°K son", round(grados_kelvin_to_grados_centigrados, 1), "°C")
    # 42 °C son 315.1 °K
    # 345 °K son 71.9 °C

#CONVERTIDOR ENTRE MM² Y MT²
millimeters_2= 425
meters_2=15.3

millimeters_2_to_meters_2=millimeters_2*1e-6
meters_2_to_millimeter_2=meters_2/1e-6

print(millimeters_2, "mm² son", millimeters_2_to_meters_2, "m²")
print(meters_2, "m² son", round(meters_2_to_millimeter_2), "mm²")
    # 425 mm² son 0.000425 m²
    # 15.3 m² son 15300000 mm²

#LABORATORIO: VALORES Y EXPRESIONES
    #x =  # codifica aquí tus datos de prueba
    # x = float(x)
    # # escribe tu código aquí
    # print("y =", y)
    # 3x3 - 2x2 + 3x - 1
x=0
x=float(x)  #flota(glotante) indica que esta variable es flotante
y= (3*x**3)-(2*x**2)+(3*x)-1
print("y = ",y)
    # y =  -1.0
x=1
x=float(x) 
y= (3*x**3)-(2*x**2)+(3*x)-1
print("y = ",y)
    # y =  3.0
x=-1
x=float(x) 
y= (3*x**3)-(2*x**2)+(3*x)-1
print("y = ",y)
    # y =  -9.0


#COMENTARIOS

# este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito hace dos días

hour = 2 
seconds = 3600 # número de segundos en una hora

print("Horas: ", hour) 
print("Segundos en", hour, "horas: ", hour * seconds) # se imprime el numero de segundos en determinado numero de horas
print("Bay, bay")
#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
#este el es fin del programa que calcula el numero de segundos en 2 horas







