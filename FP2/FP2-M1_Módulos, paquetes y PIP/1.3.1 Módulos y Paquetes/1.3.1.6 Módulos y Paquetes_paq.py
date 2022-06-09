"""Tu primer paquete: paso 1"""
# Imagina que en un futuro no muy lejano, tu y tus socios escriben una gran cantidad de funciones en Python.
# Tu equipo decide agrupar las funciones en módulos separados, y este es el resultado final:

#! /usr/bin/env python3

""" module: alpha """

def funA():
    return "Alpha"

if __name__ == "__main__":
    print("Yo prefiero ser un módulo")

# Nota: hemos presentado todo el contenido solo para el módulo alpha.py, supongamos que todos los módulos tienen un aspecto similar (contienen una función denominada funX, donde X es la primera letra del nombre del módulo).

"""Tu primer paquete: paso 2"""
# De repente, alguien se da cuenta de que estos módulos forman su propia jerarquía, por lo que colocarlos a todos en una estructura plana no será una buena idea.

# Después de algo de discusión, el equipo llega a la conclusión de que los módulos deben agruparse. Todos los participantes están de acuerdo en que la siguiente estructura de árbol refleja perfectamente las relaciones mutuas entre los módulos:

# Repasemos esto de abajo hacia arriba:

#         El grupo ugly contiene dos módulos: psi y omega.
#         El grupo best contiene dos módulos: sigma y tau.
#         El grupo good contiene dos módulos: (alpha y beta) y un subgrupo (best).
#         El grupo extra contiene dos subgrupos: (good y bad) y un módulo (iota).
# ¿Se ve mal? De ninguna manera: analiza la estructura cuidadosamente. Se parece a algo, ¿no?

# Parece la estructura de un directorio.

# Construyamos un árbol que refleje las dependencias proyectadas entre los módulos.