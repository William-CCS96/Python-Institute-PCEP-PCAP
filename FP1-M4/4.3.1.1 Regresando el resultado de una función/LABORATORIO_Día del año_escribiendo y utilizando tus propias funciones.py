# Escenario
# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.


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


def day_of_year(year, month, day):
    month_common=[31,28,31,30,31,30,31,31,30,31,30,31]
    month_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year)==False and days_in_month(year,month)!=None: 
        day_mon=0
        for i in range(month-1):
            day_mon+=month_common[i]
        return day_mon+day
    elif is_year_leap(year)==True and days_in_month(year,month)!=None: 
        day_mon=0
        for i in range(month-1):
            day_mon+=month_leap[i]
        return day_mon+day
    else:
        return None
        

a=int(input("Ingresa el año"))
b=int(input("Ingresa el mes"))
c=int(input("Ingresa el día"))

if day_of_year(a,b,c) != None:
    print("Hasta la fecha indicada hay:",day_of_year(a,b,c), "días")
else: 
    print("Recarga el programa e indica una fecha valida")