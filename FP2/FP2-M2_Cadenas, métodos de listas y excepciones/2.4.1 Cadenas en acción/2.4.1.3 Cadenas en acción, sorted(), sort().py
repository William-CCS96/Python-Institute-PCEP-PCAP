"""Ordenamiento"""
# La comparación está estrechamente relacionada con el ordenamiento (o más bien, el ordenamiento es, de hecho, un caso muy sofisticado de comparación).

# Esta es una buena oportunidad para mostrar dos formas posibles de ordenar listas que contienen cadenas. Dicha operación es muy común en el mundo real: cada vez que ves una lista de nombres, productos, títulos o ciudades, esperas que este ordenada.

# Supongamos que deseas ordenar la siguiente lista:

greek = ['omega', 'alpha', 'pi', 'gamma']

# En general, Python ofrece dos formas diferentes de ordenar las listas.

# El primero se implementa con una función llamada sorted().

# La función toma un argumento (una lista) y retorna una nueva lista, con los elementos ordenados del argumento. (Nota: esta descripción está un poco simplificada en comparación con la implementación real; lo discutiremos más adelante).
# La lista original permanece intacta.
# Observa el código en el editor y ejecútalo. El código produce el siguiente resultado:

# Demostración de la función sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)
    # ['omega', 'alpha', 'pi', 'gamma']
    # ['alpha', 'gamma', 'omega', 'pi']

# El segundo método afecta a la lista misma - no se crea una nueva lista. El ordenamiento se realiza por el método denominado sort().
# Demostración del método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
    # ['omega', 'alpha', 'pi', 'gamma']
    # ['alpha', 'gamma', 'omega', 'pi']

# Si necesitas un ordenamiento diferente, debes convencer a la función o método de cambiar su comportamiento predeterminado. Lo discutiremos pronto.

