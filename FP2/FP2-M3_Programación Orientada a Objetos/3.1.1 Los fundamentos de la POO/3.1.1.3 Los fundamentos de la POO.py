"""Jerarquías de clase"""
# La palabra clases tiene muchos significados, pero no todos son compatibles con las ideas que queremos discutir aquí. La clase que nos concierne es como una categoría, como resultado de similitudes definidas con precisión.

# Intentaremos señalar algunas clases que son buenos ejemplos de este concepto.

# Veamos por un momento los vehículos. Todos los vehículos existentes (y los que aún no existen) están relacionados por una sola característica importante: la capacidad de moverse. Puedes argumentar que un perro también se mueve; ¿Es un perro un vehículo? No lo es. Tenemos que mejorar la definición, es decir, enriquecerla con otros criterios, distinguir los vehículos de otros seres y crear una conexión más fuerte. Consideremos las siguientes circunstancias: los vehículos son entidades creadas artificialmente que se utilizan para el transporte, movidos por fuerzas de la naturaleza y dirigidos (conducidos) por humanos.

# Según esta definición, un perro no es un vehículo.

# La clase Vehículos es muy amplia. Tenemos que definir clases especializadas. Las clases especializadas son las subclases. La clase Vehículos será una superclase para todas ellas.



# Nota: la jerarquía crece de arriba hacia abajo, como raíces de árboles, no ramas. La clase más general y más amplia siempre está en la parte superior (la superclase) mientras que sus descendientes se encuentran abajo (las subclases).

# A estas alturas, probablemente puedas señalar algunas subclases potenciales para la superclase Vehículos. Hay muchas clasificaciones posibles. Elegimos subclases basadas en el medio ambiente y decimos que hay (al menos) cuatro subclases:

# Vehículos Terrestres.
# Vehículos Acuáticos.
# Vehículos Aéreos.
# Vehículos Espaciales.
# En este ejemplo, discutiremos solo la primera subclase: Vehículos Terrestres. Si lo deseas, puedes continuar con las clases restantes.

# Los vehículos terrestres pueden dividirse aún más, según el método con el que impactan el suelo. Entonces, podemos enumerar:

# Vehículos con ruedas.
# Vehículos oruga.
# Aerodeslizadores.
# La figura ilustra la jerarquía que hemos creado.

# Ten en cuenta la dirección de las flechas: siempre apuntan a la superclase. La clase de nivel superior es una excepción: no tiene su propia superclase.

