"""El Procesador de Números"""
# El tercer programa muestra un método simple que permite ingresar una línea llena de números y sumarlos fácilmente. Nota: la función input(), combinada junto con las funciones int() o float(), no es lo adecuado para este propósito.

# El procesamiento será extremadamente fácil: queremos que se sumen los números.

# Observa el código en el editor. Analicémoslo.

# Emplear listas puede hacer que el código sea más pequeño. Puedes hacerlo si quieres.

# Presentemos nuestra versión:

# La línea 03: pide al usuario que ingrese una línea llena de cualquier cantidad de números (los números pueden ser flotantes).
# La línea 04: divide la línea en una lista con subcadenas.
# La línea 05: se inicializa la suma total a cero.
# La línea 06: como la conversión de cadena a flotante puede generar una excepción, es mejor continuar con la protección del bloque try-except.
# La línea 07: itera a través de la lista...
# La línea 08: ... e intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
# La línea 09: todo está bien hasta ahora, así que imprime la suma.
# La línea 10: el programa termina aquí en caso de error.
# La línea 11: imprime un mensaje de diagnóstico que muestra al usuario el motivo de la falla.

# El código tiene una debilidad importante: muestra un resultado falso cuando el usuario ingresa una línea vacía. ¿Puedes arreglarlo?

line=input("Ingresa una línea de números, separados con espacios: ")
strings=line.split()
total=0

while True:
    try:
        if len(strings)==0:
            print("No registraste números")
        else:
            for subs in strings:
                total+=float(subs)
            print("El total es:",total)
            break
    except:
        print(subs,"no es un número.")
        line=input("Ingresa de nuevo una línea de números, separados con espacios: ")
        strings=line.split()
        total=0
        continue
