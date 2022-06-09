# pip en MS Windows
# El instalador de Python para MS Windows ya contiene pip, por lo que no es necesario seguir ningún otro paso para instalarlo. Desafortunadamente, si la variable PATH está mal configurada, es posible que pip no esté disponible.

# Para verificar que no te hemos engañado, intenta hacer esto:

# Abre la consola de Windows (CMD o PowerShell, lo que sea que prefieras)
# Ejecuta el siguiente comando:

# pip --version


# En el escenario más optimista (y realmente queremos que eso suceda) verás algo como esto:



# La ausencia de este mensaje puede significar que la variable PATH apunta incorrectamente a la ubicación de los binarios de Python o no apunta a ellos en absoluto; por ejemplo, nuestra variable PATH contiene la siguiente subcadena:


# C:\Program Files\Python3\Scripts\;C:\Program Files\Python3\;


# La forma más fácil de reconfigurar la variable PATH es reinstalar Python, indicando al instalador que lo configure por ti.