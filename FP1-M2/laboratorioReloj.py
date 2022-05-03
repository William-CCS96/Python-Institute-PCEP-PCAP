
from lib2to3.pytree import HUGE
from turtle import st


hour = int(input("Hora de inicio (horas): "))#23 #9
mins = int(input("Minuto de inicio (minutos): "))#58  #10
dura = int(input("Duración del evento (minutos): "))#642  #15
#10:40

hour_new=(((mins+dura)//60)+hour)%24
mins_new=((mins+dura)-((mins+dura)//60)*60)


print("El evento terminará a las = "+str(hour_new)+":"+str(mins_new))