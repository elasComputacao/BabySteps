n = int(raw_input())
lista = raw_input().split(' ')

menor = 10000
posicao = 0
for x in range(0, n):
  if(menor > int(lista[x])):
    menor = int(lista[x])
    posicao = x
print 'Menor valor:', menor
print 'Posicao:', posicao
