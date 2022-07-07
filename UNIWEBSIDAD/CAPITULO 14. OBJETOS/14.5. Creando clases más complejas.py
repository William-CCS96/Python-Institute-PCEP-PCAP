# Nos contratan para diseñar una clase para evaluar la relación calidad-precio de diversos hoteles. Nos dicen que los atributos que se cargarán de los hoteles son: nombre, ubicación, puntaje obtenido por votación, y precio, y que además de guardar hoteles y mostrarlos, debemos poder compararlos en términos de sus valores de relación calidad-precio, de modo tal que x < y signifique que el hotel x es peor en cuanto a la relación calidad-precio que el hotel y, y que dos hoteles son iguales si tienen la misma relación calidad-precio. La relación calidad-precio de un hotel la definen nuestros clientes como (puntaje^2) ∗ 10 / precio.

# Además, y como resultado de todo esto, tendremos que ser capaces de ordenar de menor a mayor una lista de hoteles, usando el orden que nos acaban de definir.
# Averiguamos un poco más respecto de los atributos de los hoteles:

        # El nombre y la ubicación deben ser cadenas no vacías.
        # El puntaje debe ser un número (sin restricciones sobre su valor)
        # El precio debe ser un número distinto de cero.
# Empezamos diseñar a la clase:

# El método __init__:

        # Creará objetos de la clase Hotel con los atributos que se indicaron (nombre, ubicación, puntaje, precio).
        # Los valores por omisión para la construcción son: puntaje en 0, precio en float("inf") (infinito), nombre y ubicación en * (el precio muy alto sirve para que si no se informa el precio de un hotel, se asuma el mayor valor posible.
        # Necesitamos validar que puntaje y precio sean números (utilizaremos la función es_numero que ya se usó en el caso de los puntos). Cuando un precio viene en cero se reemplaza su valor por float("inf") (de modo de asegurar que el precio nunca quede en cero).
        # Necesitamos validar que nombre y ubicación sean cadenas no vacías (para lo cual tenemos que construir una función es_cadena_no_vacia).
        # Cuando los datos no satisfagan los requisitos se levantará una excepción TypeError.
# Contará con un método __str__ para mostrar a los hoteles mediante una cadena del estilo:

""""Hotel City de Mercedes - Puntaje: 3.25 - Precio: 78 pesos"."""

# Respecto a la relación de orden entre hoteles, la clase deberá poder contar con los métodos necesarios para realizar esas comparaciones y para ordenar una lista de hoteles.

# Casi todas las tareas, podemos realizarlas con los temas vistos para la creación de la clase Punto. Para el último ítem deberemos introducir nuevos métodos especiales.

"""Ejercicio 14.1.""" 
# Escribir la función es_cadena_no_vacia(valor) que decide si un valor cualquiera es una cadena no vacía o no, e incluirla en el módulo validaciones.

# El fragmento inicial de la clase programada en Python queda así:



def es_cadena_no_vacia(valor):
    return len(valor)!=0

def es_numero(valor):
    return isinstance(valor,(int,float,complex))

class Hotel(object):
    """Hotel: sus atributos son: nombre, ubicación, puntaje y precio."""
    def __init__(self,nombre="*",ubicacion="*",puntaje=0,precio=float("inf")):
        """ nombre y ubicacion deben ser cadenas no vacías,
            puntaje y precio son números.
            Si el precio es 0 se reemplaza por infinito. """
        if es_cadena_no_vacia(nombre):
            self.nombre=nombre
        else:
            raise TypeError("El nombre debe ser una cadena no vacía")

        if es_cadena_no_vacia(ubicacion):
            self.ubicacion=ubicacion
        else:
            raise TypeError("La ubiación debe ser una cadena no vacía")

        if es_numero(puntaje):
            self.puntaje=puntaje
        else:
            raise TypeError("El puntaje debe ser un número")
        
        if es_numero(precio):
            if precio!=0:
                self.precio=precio
            else:
                self.precio=float("inf")
        else:
            raise TypeError("El precio debe ser un número")

    def __str__(self):
        """Muestra el Hotel según lo requerido"""
        return self.nombre+" de "+self.ubicacion+ \
            " - Puntaje: "+str(self.puntaje)+" - Precio: "+ \
            str(self.precio)+" pesos."

    """Con este código tenemos ya la posibilidad de construir hoteles, con los atributos de los tipos correspondientes, y de mostrar los hoteles según nos lo han solicitado."""

# h1=Hotel("Hotel City","Madrid",3.78,115.000)
# print(h1)
    # Hotel City de Madrid - Puntaje: 3.78 - Precio: 115.0 pesos.

    """14.5.1. Métodos para comparar objetos"""
    # En particular, cuando se quiere que los objetos puedan ser ordenados, el método que se debe definir es __cmp__, que debe devolver:

    # Un valor entero menor a cero, si el primer parámetro es menor al segundo.
    # Un valor entero mayor a cero, si el primer parámetro es mayor que el segundo.
    # Cero, si ambos parámetros son iguales.
    
    # Para crear el método __cmp__, definiremos primero un método auxiliar ratio(self) que calcula la relación calidad-precio de una instancia de Hotel según la fórmula indicada:    

    def ratio (self):
        """ Calcula la relación calidad-precio de un hotel de acuerdo
        a la fórmula que nos dio el cliente. """
        return ((self.puntaje**2)*10.)/self.precio
    # A partir de este método es muy fácil crear un método __cmp__ que cumpla con la especificación previa.
    def __lt__(self,otro):
        return self.ratio()<otro.ratio()
    def __eq__(self,otro):
        return self.ratio()==otro.ratio()

    """14.5.3. Otras formas de comparación"""
    

h1=Hotel("Hotel City","Madrid",14,150)   
h2=Hotel("Hotel Mascardi","Bariloche",15,150)


print(h1<h2)
print(h1.ratio(),h2.ratio())
    
h1=Hotel("Hotel 1* normal", "MDQ", 1, 10)
h2=Hotel("Hotel 2* normal", "MDQ", 2, 40)
h3=Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
h4=Hotel("Hotel vale la pena" ,"MDQ", 4, 130)
lista = [ h1, h2, h3, h4 ]
lista.sort()
for hotel in lista:
    print(hotel)
    # Hotel 3* carisimo de MDQ - Puntaje: 3 - Precio: 130 pesos.
    # Hotel 1* normal de MDQ - Puntaje: 1 - Precio: 10 pesos.
    # Hotel 2* normal de MDQ - Puntaje: 2 - Precio: 40 pesos.
    # Hotel vale la pena de MDQ - Puntaje: 4 - Precio: 130 pesos. 

