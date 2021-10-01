# Questao 1066

lista = []

for i in range(5):
  lista.append(int(input()))

contP = 0
contI = 0
contPos = 0
contNeg = 0

for i in lista:
  if i>0:
    contPos +=1
  elif i<0:
    contNeg +=1
  if i%2 == 0:
    contP +=1
  else:
    contI +=1

print(contP, "valor(es) par(es)")
print(contI,"valor(es) impar(es)")
print(contPos, "valor(es) positivo(s)")
print(contNeg, "valor(es) negativo(s)")
