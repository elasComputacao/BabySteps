import math
n = input().split()
a,b,c = float(n[0]),float(n[1]),float(n[2])

x = (b ** 2) - (4 * a * c)

if x < 0 or a==0:
    print('Impossivel calcular')
    exit()

else:
    x = math.sqrt(x)
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)

print('R1 = {:.5f}\nR2 = {:.5f}'.format(x1,x2))
