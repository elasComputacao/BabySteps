n = int(input())
cat = {'ano(s)':365, 'mes(es)':30, 'dia(s)':1}
for k,i in cat.items():
    valor = n//i
    n-=i*valor
    print(f'{valor} {k}')