# IMC = Peso en kilogramos / Altura en metros

#Body Mass Index (BMI)

def bmi(weight, height):
    return weight / height ** 2  # weight / peso


print(bmi(52.5, 1.65))
# 19.283746556473833

    # La función hace lo que deseamos, pero es un poco sencilla - asume que los valores de ambos parámetros son significativos. Se debe comprobar que son confiables.
    # Vamos a comprobar ambos y regresar None si cualquiera de los dos es incorrecto.

#-----------------------------
# Algunas funciones simples: calcular el IMC y convertir unidades del Sistema Inglés al Sistema Métrico

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:  #Simbolo \ (Alt+92) para continura código en la siguiente linea
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

            # Segundo, observa como el símbolo de diagonal invertida (\) es empleado. Si se termina una línea de código con el, Python entenderá que la línea continua en la siguiente.

            # Esto puede ser útil cuando se tienen largas líneas de código y se desea que sean más legibles.

#---------------------------
# Sin embargo, hay algo que omitimos: las medias en sistema inglés. La función no es útil para personas que utilicen libras, pies y pulgadas.
# Escribimos dos funciones sencillas para convertir unidades del sistema inglés al sistema métrico. Comencemos con las pulgadas.
    # 1 lb = 0.45359237 kg

def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))
    # 0.45359237

# Haremos lo mismo ahora con los pies y pulgadas: 1 ft = 0.3048 m, y 1 in = 2.54 cm = 0.0254 m.
# La función se llamará ft_and_inch_to_m:

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))
    # 0.3302
        # Nota: queríamos nombrar el segundo parámetro solo in, no inch, pero no pudimos. ¿Sabes por qué?
        # in es una palabra clave reservada de Python â no se puede usar como nombre.

#-------------------------------------
# Vamos a convertir seis pies a metros:
print(ft_and_inch_to_m(6, 0))
    # 1.8288000000000002

    # Es muy posible que en ocasiones se desee utilizar solo pies sin pulgadas. ¿Python nos ayudará? Por supuesto que si.
    # Se ha modificado el código un poco:

def ft_and_inch_to_m(ft, inch = 0.0): #Por defecto toma el 0.0 a menos que le indiquemos lo contrario
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(6))

#-----------------------------------
# Finalmente, el código es capaz de responder a la pregunta: ¿Cuál es el IMC de una persona que tiene 5'7" de altura y un peso de 176 lbs?
# Este es el código que hemos construido:

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(164), height = ft_and_inch_to_m(5.85)))
    # 23.397417849859607
    