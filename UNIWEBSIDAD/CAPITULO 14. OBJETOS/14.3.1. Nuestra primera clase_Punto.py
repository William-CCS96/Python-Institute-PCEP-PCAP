
"""14.3.1. Nuestra primera clase: Punto"""

"""class Punto (object): #La palabra object entre paréntesis indica que la clase que estamos creando es un objeto básico, no está basado en ningún objeto más complejo.
    Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas.
    def __init__(self, x=0, y=0):
        "Constructor de Punto, x e y deben ser numéricos"
        # Y en el caso de que alguno de los valores no sea numérico, lanzaremos una excepción del tipo TypeError. El nuevo constructor quedará así:
        self.x= x 
        self.y= y"""

# p1=Punto(5,7)
# print(p1)
# print(p1.x)
# print(p1.y)
# Nota
# Por convención, en los nombres de las clases definidas por el programador, se escribe cada palabra del nombre con la primera letra en mayúsculas. Ejemplos: Punto, ListaEnlazada, Hotel.

"""14.3.2. Agregando validaciones al constructor"""
# q1=Punto("A",False)
# print(q1.x)
# print(q1.y)
# print(isinstance(q1.y,(bool)))#Función que revisa si una instancia pertenece a una clase en especifico 
# print(isinstance(p1.x,(float,(complex,int))))


# Si queremos impedir que esto suceda, debemos agregar validaciones al constructor, como las vistas en unidades anteriores.
# Verificaremos que los valores pasados para x e y sean numéricos, utilizando la función es_numero, que incluiremos en un módulo llamado validaciones:



def es_numero(valor):
    """Indica si un valor es número o no."""
    return isinstance(valor,(int,float,complex))


class Punto (object): #La palabra object entre paréntesis indica que la clase que estamos creando es un objeto básico, no está basado en ningún objeto más complejo.
    """ Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas."""
    def __init__(self, x=0, y=0):
        "Constructor de Punto, x e y deben ser numéricos"
        # Y en el caso de que alguno de los valores no sea numérico, lanzaremos una excepción del tipo TypeError. El nuevo constructor quedará así:
        if es_numero(x) and es_numero(y):
            self.x= x 
            self.y= y
        else:
            raise TypeError("x e y deben ser valores númericos")

    """14.3.3. Agregando operaciones"""
    # def distance(self,otro):
    #     """Devuelve la distancia entre ambos puntos"""
    #     dx=self.x-otro.x
    #     dy=self.y-otro.y
    #     return round(math.sqrt(dx*dx+dy*dy),2)
    # Podemos ver, sin embargo, que la operación para calcular la distancia incluye la operación de restar dos puntos y la de obtener la norma de un vector. Sería deseable incluir también estas dos operaciones dentro de la clase Punto.
    def restar(self,otro):
        """Devuelve un nuevo puntos, con la resta de los dos puntos"""
        return(self.x-otro.x,self.y-otro.y)
    # A continuación, definimos el método para calcular la norma del vector que se forma uniendo un punto con el origen.
    
    def norma(self):
        """ Devuelve la norma del vector que va desde el origen
        hasta el punto. """
        return (self.x*self.x + self.y*self.y)**0.5

    def distance(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        r=self.restar(otro)
        r1=Punto(r[0],r[1])
        return r1.norma()

p=Punto(5,7)
q=Punto(2,3)
print(p.restar(q))
print(p.norma(),q.norma())
print(p.distance(q))


