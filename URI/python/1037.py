x = float(input())
if 0<= x <= 25:
    print('Intervalo [0,25]')
if 25< x <= 50:
    print('Intervalo (25,50]')
if 50< x <= 75:
    print('Intervalo (50,75]')
if 75< x <= 100:
    print('Intervalo (75,100]')
if x >100 or x<0:
    print('Fora de intervalo')