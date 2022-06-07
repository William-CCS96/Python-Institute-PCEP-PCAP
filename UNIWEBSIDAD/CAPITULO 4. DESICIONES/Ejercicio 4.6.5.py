# Ejercicio 4.6.5. Escribir funciones que resuelvan los siguientes problemas:


# Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

from ast import If


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

print(is_year_leap(1996))
    # True

# Dado un mes, devolver la cantidad de dias correspondientes.
def days_month(month):
    month_28=[2]
    month_30=[4,6,9,11]
    month_31=[1,3,5,7,8,10,12]
    if month in month_28: return 28
    elif month in month_30: return 30
    elif month in month_31: return 31
    else: return "El valor introducido no es valido" 

print(days_month(5))
    # 31

# Dada una fecha (dia, mes, año), indicar si es válida o no.
def days_in_month(year, month):
    leap_common=is_year_leap(year)
    global month_30
    global month_31
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
print(days_in_month(1995,2))
    # 28
        
def valid_date(year,month,day):
    if days_in_month(year,month)!=None and days_in_month(year,month)>=day and day>0:
        return "Date true"
    else:
        return "Date false"

valid_date(1995,2,29)
    # Date false


# Dada una fecha, indicar la cantidad de dias transcurridos en ese año hasta esa fecha.
def day_of_year(year, month, day):
    if valid_date(year, month, day)=="Date false":
        return "Date false"
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
        return "Date false"

print(day_of_year(1995,2,30))
    

# Dada una fecha, indicar los dias que faltan hasta fin de año.
def day_leftovert_year(year, month, day):
    if valid_date(year, month, day)=="Date false":
        return print("Date false")
    elif day_of_year(year, month, day)!=None:
        if is_year_leap(year)==True:
            leftovert=366-day_of_year(year, month, day)
        else:
            leftovert=365-day_of_year(year, month, day)
    return leftovert

day_leftovert_year(1996,3,28)
    # The remaining days of the indicated date are: 278

# Dada una fecha, indicar los dias que faltan hasta fin de mes.
def day_leftovert_month(year, month, day):
    if valid_date(year, month, day)=="Date false":
        return "Date false"
    if is_year_leap(year)==False:
        if month==2:
            leftovert=28-day
    elif is_year_leap(year)==True:
        if month==2:
            leftovert=29-day
    if month in month_30:
        leftovert=30-day
    elif month in month_31:
        leftovert=31-day
    return leftovert

print(day_leftovert_month(1996,2,28))  
    # 1

# Dadas dos fechas (dia1, mes1, año1, dia2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y dias.


def days_between_dates(year1, month1, day1,year2, month2, day2):
    if valid_date(year1, month1, day1)=="Date false" or valid_date(year2, month2, day2)=="Date false":
        return "Date false"
    days_totals=0
    while True:
        if year1==year2 and month1==month2 and day1==day2:
            break
        if day1<(days_in_month(year1,month1)):
            day1+=1
            days_totals+=1
        elif day1==(days_in_month(year1, month1)):
            day1=1
            days_totals+=1
            month1+=1
            if month1==13:
                month1=1
                year1+=1
    day_end=0
    year_end=0
    month_end=0
    count=0
    while True:
        # print(year_end,month_end,day_end)
        # print(count)
        if days_totals==count:
            break
        if day_end<(days_in_month(year_end,month_end+1)):
            day_end+=1
            count+=1
        elif day_end==(days_in_month(year_end, month_end+1)):
            day_end=1
            count+=1
            month_end+=1
            if month_end==13:
                month_end=1
                year_end+=1
    return print("Between the two dates there",year_end,"years,",month_end,"months and",day_end,"days")
                
        
days_between_dates(2015,1,1,2016,1,1)
#Between the two dates there 0 years, 11 months and 31 days



