"""Excepciones"""
# Python 3 define 63 excepciones integradas, y todas ellas forman una jerarquía en forma de árbol, aunque el árbol es un poco extraño ya que su raíz se encuentra en la parte superior.

# Algunas de las excepciones integradas son más generales (incluyen otras excepciones) mientras que otras son completamente concretas (solo se representan a sí mismas). Podemos decir que cuanto más cerca de la raíz se encuentra una excepción, más general (abstracta) es. A su vez, las excepciones ubicadas en los extremos del árbol (podemos llamarlas hojas) son concretas.

# Observa la figura:

# Muestra una pequeña sección del árbol completo de excepciones. Comencemos examinando el árbol desde la hoja ZeroDivisionError.


# Nota:

# ZeroDivisionError es un caso especial de una clase de excepción más general llamada ArithmeticError.
# ArithmeticError es un caso especial de una clase de excepción más general llamada solo Exception.
# Exception es un caso especial de una clase más general llamada BaseException.
# Podemos describirlo de la siguiente manera (observa la dirección de las flechas; siempre apuntan a la entidad más general):

# BaseException
# ↑
# Exception
# ↑
# ArithmeticError
# ↑
# ZeroDivisionError

# Te mostraremos el funcionamiento esta generalización. Comencemos con un código realmente simple.

