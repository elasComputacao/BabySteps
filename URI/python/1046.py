start, end = [int(x) for x in input().split(" ")] 

time = 0

if(start<end):
    time=end-start
else:
    time=end+24-start
    
print("O JOGO DUROU "+str(time)+" HORA(S)")
