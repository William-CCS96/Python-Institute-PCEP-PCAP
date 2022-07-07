"""La pila: el enfoque procedimental frente al enfoque orientado a objetos"""
# La pila procedimental está lista. Por supuesto, hay algunas debilidades, y la implementación podría mejorarse de muchas maneras (aprovechar las excepciones es una buena idea), pero en general la pila está completamente implementada, y puedes usarla si lo necesitas.

# Pero cuanto más la uses, más desventajas encontrarás. Éstas son algunas de ellas:

        # La variable esencial (la lista de la pila) es altamente vulnerable; cualquiera puede modificarla de forma incontrolable, destruyendo la pila; esto no significa que se haya hecho de manera maliciosa; por el contrario, puede ocurrir como resultado de un descuido, por ejemplo, cuando alguien confunde nombres de variables; imagina que accidentalmente has escrito algo como esto:

        # stack[0] = 0


        # El funcionamiento de la pila estará completamente desorganizado.

        # También puede suceder que un día necesites más de una pila; tendrás que crear otra lista para el almacenamiento de la pila, y probablemente otras funciones push y pop.

        # También puede suceder que no solo necesites funciones push y pop, pero también algunas otras funciones; ciertamente podrías implementarlas, pero intenta imaginar qué sucedería si tuvieras docenas de pilas implementadas por separado.


"""El enfoque orientado a objetos ofrece soluciones para cada uno de los problemas anteriores. Vamos a nombrarlos primero:"""

        # La capacidad de ocultar (proteger) los valores seleccionados contra el acceso no autorizado se llama encapsulamiento; no se puede acceder a los valores encapsulados ni modificarlos si deseas utilizarlos exclusivamente.

        # Cuando tienes una clase que implementa todos los comportamientos de pila necesarios, puedes producir tantas pilas como desees; no necesitas copiar ni replicar ninguna parte del código.

        # La capacidad de enriquecer la pila con nuevas funciones proviene de la herencia; puedes crear una nueva clase (una subclase) que herede todos los rasgos existentes de la superclase y agregar algunos nuevos.


