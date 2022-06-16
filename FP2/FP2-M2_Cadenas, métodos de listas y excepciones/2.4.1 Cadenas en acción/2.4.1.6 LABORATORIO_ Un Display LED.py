"""LABORATORIO"""
# Tiempo Estimado
# 30 minutos

# Nivel de dificultad
# Medio

# Objetivos
    # Mejorar las habilidades del alumno al trabajar con cadenas.
    # Usar cadenas para representar datos que no son texto.
# Escenario
# Seguramente has visto un display de siete segmentos.

# Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia: https://en.wikipedia.org/wiki/Seven-segment_display.

# Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

# Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

    # ### ### # # ### ### ### ### ### ### 
    #   #   # # # #   #     # # # # # # # 
    # ### ### ### ### ###   # ### ### # # 
    # #     #   #   # # #   # # #   # # # 
    # ### ###   # ### ###   # ### ### ###

# Nota: el número 8 muestra todas las luces LED encendidas.

# Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.

# Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.

# Datos de prueba
# Entrada de muestra:
# 123

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

# 9081726354

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 

list=[["###","# #","# #","# #","###"],\
["  #","  #","  #","  #","  #"],\
["###","  #","###","#  ","###"],\
["###","  #","###","  #","###"],\
["# #","# #","###","  #","  #"],\
["###","#  ","###","  #","###"],\
["###","#  ","###","# #","###"],\
["###","  #","  #","  #","  #"],\
["###","# #","###","# #","###"],\
["###","# #","###","  #","###"]]

num_print=input("Introduce el número que deseas observar: ")

def board_elect(num):
  # if len(num)==0 or len(num)>10:
  #   return None
  for n in num: print(list[int(n)][0], end=" ")
  print("\n", end="")
  for n in num: print(list[int(n)][1], end=" ")
  print("\n", end="")
  for n in num: print(list[int(n)][2], end=" ")
  print("\n", end="")
  for n in num: print(list[int(n)][3], end=" ")
  print("\n", end="")
  for n in num: print(list[int(n)][4], end=" ")
  print("\n", end="")

board_elect(num_print)