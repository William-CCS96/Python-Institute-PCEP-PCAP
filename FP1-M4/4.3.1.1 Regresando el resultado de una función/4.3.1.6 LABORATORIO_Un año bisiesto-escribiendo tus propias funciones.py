# Escenario
# Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

# Parte del esqueleto de la función ya está en el editor.

# Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

# El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.

# def is_year_leap(year):
#     year_result=[]
#     for i in range(len(year)):
#         if year[i]<1582:
#             year_result.append(False)
#         elif year[i]%4!=0:
#             year_result.append(False)
#         elif year[i]%100!=0:
#             year_result.append(True)
#         elif year[i]%400!=0:
#             year_result.append(False)
#         else:
#             year_result.append(True)
#     return year_result

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


print(is_year_leap(1959))
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
     yr = test_data[i]
     print(yr,"->",end="")
     result = is_year_leap(yr)
     if result == test_results[i]:
         print("OK")
     else:
         print("Fallido")

# 1900 ->OK
# 2000 ->OK
# 2016 ->OK
# 1987 ->OK