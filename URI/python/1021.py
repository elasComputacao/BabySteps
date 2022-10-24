A = float(input())

print ('NOTAS:')
n100 = int(A / 100)
resto = (A % 100)
print (n100,'nota(s) de R$ 100.00')

n50 = int(resto / 50)
print (n50,'nota(s) de R$ 50.00')
resto = float(resto % 50)

n20 = int(resto / 20)
print (n20,'nota(s) de R$ 20.00')
resto = float(resto % 20)

n10 = int(resto / 10)
print (n10,'nota(s) de R$ 10.00')
resto = float(resto % 10)

n5 = int(resto / 5)
print (n5,'nota(s) de R$ 5.00')
resto = float(resto % 5)

n2 = int(resto / 2)
print (n2,'nota(s) de R$ 2.00')
resto = float(resto % 2)

print ('MOEDAS:')
n1 = int(resto / 1)
print (n1,'moeda(s) de R$ 1.00')

B = A - int(A) + 0.001

n050 = int(B / 0.5)
print (n050,'moeda(s) de R$ 0.50')
restoB = (B % 0.5)

n025 = int(restoB / 0.25)
print (n025,'moeda(s) de R$ 0.25')
restoB = (restoB % 0.25)

n010 = int(restoB / 0.10)
print (n010,'moeda(s) de R$ 0.10')
restoB = (restoB % 0.10)

n005 = int(restoB / 0.05)
print (n005,'moeda(s) de R$ 0.05')
restoB = (restoB % 0.05)

n001 = int(restoB / 0.01)
print (n001,'moeda(s) de R$ 0.01')
