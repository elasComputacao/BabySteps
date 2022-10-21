entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
d = int(entrada[3])

if b>c and d>a and (c+d)>(a+b) and c>0 and d>0 and a%2==0:
   print('Valores aceitos')
else:
    print('Valores nao aceitos')