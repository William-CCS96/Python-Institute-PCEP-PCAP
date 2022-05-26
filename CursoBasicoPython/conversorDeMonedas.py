
money=int(input("""
Bienvenido a tu conversor de monedas 💲 

Que modena tienes:
1. Pesos colombianos
2. Dolares
3. Euro
4. BTC
Marca el número correspondiente a tu moneda: 
""")) #Sacar emoji con windows + .

# valor 1. Pesos colombianos
valor_dolar_pesos = 3679
valor_euro_pesos = 4383
valor_btc_pesos = 136134100
#Valor 2. Dolares
valor_peso_dolares = 0.00024
valor_euro_dolares = 1.05
valor_btc_dolares = 29841
#Valor 3. Euro
valor_peso_euro = 0.00023
valor_dolares_euro = 0.95
valor_btc_euro= 28236.81
#Valor 4. Btc
valor_peso_btc = 0.0000000085
valor_dolares_btc = 0.000034
valor_euro_btc= 0.000035


if money==1:
    cash=float(input("¿Cuántos pesos Col tienes?: "))
    calculo_valor_dolar_pesos=str(round(cash/valor_dolar_pesos,2))
    calculo_valor_euro_pesos=str(round(cash/valor_euro_pesos,2))
    calculo_valor_btc_pesos=str(round(cash/valor_btc_pesos,9))
    print("Tienes: $"+calculo_valor_dolar_pesos+" dolares")
    print("Tienes: €"+calculo_valor_euro_pesos+" euros")
    print("Tienes: "+calculo_valor_btc_pesos+" BTC")
elif money ==2:
    cash=float(input("¿Cuántos dolares tienes?: "))
    calculo_valor_peso_dolares=str(round(cash/valor_peso_dolares,2))
    calculo_valor_euro_dolares=str(round(cash/valor_euro_dolares,2))
    calculo_valor_btc_dolares=str(round(cash/valor_btc_euro,9))
    print("Tienes: $"+calculo_valor_peso_dolares+" pesos Col")
    print("Tienes: €"+calculo_valor_euro_dolares+" euros")
    print("Tienes: "+calculo_valor_btc_dolares+" BTC")
elif money ==3:
    cash=float(input("¿Cuántos euros tienes?: "))
    calculo_valor_peso_euro=str(round(cash/valor_peso_euro,2))
    calculo_valor_dolares_euro=str(round(cash/valor_dolares_euro,2))
    calculo_valor_btc_euro=str(round(cash/valor_btc_euro,9))
    print("Tienes: $"+calculo_valor_peso_euro+" pesos Col")
    print("Tienes: $"+calculo_valor_dolares_euro+" dolares")
    print("Tienes: "+calculo_valor_btc_euro+" BTC")
elif money ==4:
    cash=float(input("¿Cuántos btc tienes?: "))
    calculo_valor_peso_btc=str(round(cash/valor_peso_btc,2))
    calculo_valor_dolares_btc=str(round(cash/valor_dolares_btc,2))
    calculo_valor_euro_btc=str(round(cash/valor_euro_btc,2))
    print("Tienes: $"+calculo_valor_peso_btc+" pesos Col")
    print("Tienes: $"+calculo_valor_dolares_btc+" dolares")
    print("Tienes: €"+calculo_valor_euro_btc+" euros")
else:
    print("Reinicia el programa e ingresa una opción correcta.")



    
