# pip en Linux
# Diferentes distribuciones de Linux pueden comportarse de manera diferente cuando se trata de usar pip. Algunas de ellas (como Gentoo), que están estrechamente vinculadas a Python y que lo usan internamente, pueden tener pip preinstalado y están instantáneamente listas para funcionar.

# No olvides que algunas distribuciones de Linux pueden utilizar más de una versión de Python al mismo tiempo, por ejemplo, un Python 2 y un Python 3 coexistiendo uno al lado del otro. Estos sistemas pueden iniciar Python 2 como la versión predeterminada y puede ser necesario especificar explícitamente el nombre del programa como python3. En este caso, puede haber dos pip diferentes identificados como pip (o pip2) y pip3. Compruébalo cuidadosamente.

# Abre la ventana de la terminal y emite el siguiente comando:

# pip --version



# pip --version, python 2.7



# Una respuesta similar a la que se muestra en la imagen anterior determina que has iniciado pip desde Python 2, por lo que el siguiente intento debería verse de la siguiente manera:

# pip3 --version



# pip --version, python 3.6

# Como puedes ver, ahora estamos seguros de que estamos utilizando la versión adecuada de pip.