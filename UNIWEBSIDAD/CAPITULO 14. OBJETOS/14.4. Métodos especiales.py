def es_numero(valor):
    """Indica si un valor es número o no."""
    return isinstance(valor,(int,float,complex))

class Punto (object): 
    def __init__(self, x=0, y=0):
        if es_numero(x) and es_numero(y):
            self.x= x 
            self.y= y
        else:
            raise TypeError("x e y deben ser valores númericos")
    def restar(self,otro):
        """Devuelve un nuevo puntos, con la resta de los dos puntos"""
        return(self.x-otro.x,self.y-otro.y)
    
    def norma(self):
        """ Devuelve la norma del vector que va desde el origen
        hasta el punto. """
        return (self.x*self.x + self.y*self.y)**0.5

    def distance(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        r=self.restar(otro)
        r1=Punto(r[0],r[1])
        return r1.norma()
        
    """14.4.1. Un método para mostrar objetos"""
    # En nuestro caso decidimos mostrar el punto como un par ordenado, por lo que escribimos el siguiente método dentro de la clase Punto:
    def __str__(self):
        """Muestra el punto como un par ordenado."""
        """Una vez definido este método, nuestro punto se mostrará como un par ordenado cuando se necesite una representación de cadenas."""
        """Es decir que la función str internamente invoca al método __str__ del objeto que recibe como parámetro. Y de la misma manera len invoca internamente al método __len__, si es que está definido."""
        return "("+str(self.x)+", "+str(self.y)+")"
        
    
# p=Punto(-6,18)
# print(str(p))
# # (-6, 18)
# print(dir(p))

    """14.4.2. Métodos para operar matemáticamente"""
    """Ya hemos visto un método que permitía restar dos puntos. Si bien esta implementación es perfectamente válida, no es posible usar esa función para realizar una resta con el operador -."""
    """Si queremos que este operador (o el equivalente para la suma) funcione, será necesario implementar algunos métodos especiales"""

    def __add__(self,otro):
        """Devuelve la suma de ambos puntos"""
        return Punto(self.x+otro.x,self.y+otro.y)
    def __sub__(self,otro):
        """Devuelve la resta de ambos puntos"""
        return Punto(self.x-otro.x,self.y-otro.y)
    
p=Punto(5,8)
q=Punto(4,5)
suma=p+q
resta=p-q
print(suma,resta)
print(resta.norma())