#Questão 1045

entradas = input().split()
auxA, auxB, auxC = entradas

auxA = float(auxA)
auxB = float(auxB)
auxC = float(auxC)

a = float(0)
b = float(0)
c = float(0)

if auxA == auxB == auxC:
  a = auxA
  b = auxB
  c = auxC

if auxA >= auxB and auxA >= auxC:
  if auxB >= auxC:
    a = auxA
    b = auxB
    c = auxC
  else:
    a = auxA
    b = auxC
    c = auxB

if auxB >= auxA and auxB >= auxC:
  if auxA >= auxC:
    a = auxB
    b = auxA
    c = auxC
  else:
    a = auxB
    b = auxC
    c = auxA

if auxC >= auxA and auxC >= auxB:
  if auxA >= auxB:
    a = auxC
    b = auxA
    c = auxB
  else:
    a = auxC
    b = auxB
    c = auxA


if a >= (b + c):
  print("NAO FORMA TRIANGULO")

else:
  if (a**2) == (b**2 + c**2):
    print("TRIANGULO RETANGULO")

  if (a**2) > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")

  if (a**2) < (b**2 + c**2):
    print("TRIANGULO ACUTANGULO")

  if a == b == c:
    print("TRIANGULO EQUILATERO")

  if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print("TRIANGULO ISOSCELES")

