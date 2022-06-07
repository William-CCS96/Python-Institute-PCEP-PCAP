# Permítenos presentarte un valor muy curioso (para ser honestos, un valor que es ninguno) llamado None.

# Nota: None es una palabra clave reservada.

# Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:

# Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
# Cuando se compara con una variable para diagnosticar su estado interno.

value = None
if value is None:
    print("Lo siento, no contienes ningún valor")

# No olvides esto: si una función no devuelve un cierto valor utilizando una cláusula de expresión return, se asume que devuelve implícitamente None.

#-----------------------------
# Es obvio que la función strangeFunction retorna True cuando su argumento es par.
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))
    # True
    # None