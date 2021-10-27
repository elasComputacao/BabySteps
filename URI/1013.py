numeros = input('').split(' ')

maior = int(numeros[0])

for x in numeros:
  if int(x) > maior:
    maior = int(x)

#Deve ser usada a versão 3.8 ou superior do python para funcionar a notação de f-string
print(f'{maior} eh o maior')
