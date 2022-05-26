# Escenario
# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LABORATORIO 4.1.3.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función; este truco acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.



def is_year_leap(year):
        if year<1582:
            return(False)
        elif year%4!=0:
            return(False)
        elif year%100!=0:
            return(True)
        elif year%400!=0:
            return(False)
        else:
            return(True)

def days_in_month(year, month):
    leap_common=is_year_leap(year)
    month_30=[4,6,9,11]
    month_31=[1,3,5,7,8,10,12]
    if leap_common==True and month==2:
        return 29
    elif leap_common==False and month==2:
        return 28
    elif month in month_30:
        return 30
    elif month in month_31:
        return 31
    else:
        return None
    
print(days_in_month(1987,11))

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
# 1900 2 ->OK
# 2000 2 ->OK
# 2016 1 ->OK
# 1987 11 ->OK

    
    

