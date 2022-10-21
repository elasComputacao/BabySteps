start_hour, start_min, end_hour, end_min = [int(x) for x in input().split(" ")] 

dif=((end_hour*60)+end_min)-((start_hour*60)+start_min)

if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60

print("O JOGO DUROU "+str(time)+" HORA(S) E "+str(minute)+" MINUTO(S)")
