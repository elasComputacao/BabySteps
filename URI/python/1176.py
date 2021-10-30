def fib(x):
  if(x == 0):
    return 0
  ant = 1
  atual = 1
  prox = ant + atual  
  for x in range(2, x):
    prox = ant + atual
    ant = atual 
    atual = prox
  return atual
vezes = int(input())
for z in range(0, vezes):
  i = int(input())
  print('Fib(%d) = %d' %(i, fib(i)))
