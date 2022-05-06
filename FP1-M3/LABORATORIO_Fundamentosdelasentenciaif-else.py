#Utilizar la sentencia if-else para ramificar la ruta de control.
#Construir un programa completo que resuelva problemas simples de la vida real.

#Escenario
# Érase una vez una tierra de leche y miel, habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto, su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:
# Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
# Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

#Tu tarea es escribir una calculadora de impuestos.
# Debe aceptar un valor de punto flotante: el ingreso.
# A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el código de esqueleto del editor.
# Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.
# Observa el código en el editor: solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes
# Prueba tu código con los datos que hemos proporcionado.

income = float(input("Introduce el ingreso anual:"))
impuesto=0
if income<85528:
    impuesto=(income*0.18)-556.20
if income>85528:
    impuesto=14839.20+((income-85528)*0.32)
if impuesto<0:
    impuesto=0.0

print("El impuesto a pagar será de: ", round(impuesto,0),"pesos.")

    

