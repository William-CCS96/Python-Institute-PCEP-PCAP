"""Variables de clase  __dict__"""

# Hemos dicho antes que las variables de clase existen incluso cuando no se creó ninguna instancia de clase (objeto).

# Ahora aprovecharemos la oportunidad para mostrarte la diferencia entre estas dos variables __dict__, la de la clase y la del objeto.

# Observa el código en el editor. La prueba está ahí.

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)

        # Definimos una clase llamada ExampleClass.

        # La clase define una variable de clase llamada varia.
        # El constructor de la clase establece la variable con el valor del parámetro.
        # Nombrar la variable es el aspecto más importante del ejemplo porque:
                # El cambiar la asignación a self.varia = val crearía una variable de instancia con el mismo nombre que la de la clase.
                # El cambiar la asignación a varia = val operaría en la variable local de un método; (te recomendamos probar los dos casos anteriores; esto te facilitará recordar la diferencia).

        # La primera línea del código fuera de la clase imprime el valor del atributo ExampleClass.varia . Nota: utilizamos el valor antes de instanciar el primer objeto de la clase.

# Como puedes ver __dict__ contiene muchos más datos que la contraparte de su objeto. La mayoría de ellos son inútiles ahora, el que queremos que verifiques cuidadosamente muestra el valor actual de varia.

# Nota que el __dict__ del objeto está vacío, el objeto no tiene variables de instancia.

"""
{'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x00000247204EECB0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

{'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x00000247204EECB0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

{}
"""

