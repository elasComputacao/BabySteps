lista = []
n = 0
while(n < 20):
  val = int(input())
  lista.append(val)
  n += 1
n = 0
j = 19
while(n < len(lista)/2):
  lista[n], lista[j] = lista[j], lista[n]
  j -= 1
  n+=1
n = 0
while(n < len(lista)):
  print('N[%.d] = %.d' %(n, lista[n]))
  n+=1
