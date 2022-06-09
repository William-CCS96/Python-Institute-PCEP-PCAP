"""Puntos Clave"""

# 1. Las computadoras almacenan caracteres como números. Hay más de una forma posible de codificar caracteres, pero solo algunas de ellas ganaron popularidad en todo el mundo y se usan comúnmente en TI: estas son ASCII (se emplea principalmente para codificar el alfabeto latino y algunos de sus derivados) y UNICODE (capaz de codificar prácticamente todos los alfabetos que utilizan los seres humanos).


# 2. Un número correspondiente a un carácter en particular se llama punto de código.


# 3. UNICODE utiliza diferentes formas de codificación cuando se trata de almacenar los caracteres usando archivos o memoria de computadora: dos de ellas son UCS-4 y UTF-8 (esta última es la más común ya que desperdicia menos espacio de memoria).



"""Ejercico 1"""
# ¿Qué es BOM?
# BOM (Byte Order Mark), Una Marca de Orden de Bytes es una combinación especial de bits que anuncia la codificación utilizada por el contenido de un archivo (por ejemplo, UCS-4 o UTF-B).

"""Ejercico 2"""
# ¿Está Python 3 internacionalizado?
# Sí, está completamente internacionalizado: podemos usar caracteres UNICODE dentro de nuestro código, leerlos desde la entrada y enviarlos a la salida.