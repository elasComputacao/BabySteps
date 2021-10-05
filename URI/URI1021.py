n = float(raw_input())

nota100 = n/100
n %= 100
nota50 = n/50
n %= 50
nota20 = n/20
n %= 20
nota10 = n/10
n %= 10
nota5 = n/5
n %= 5
nota2 = n/2
n %= 2
nota1 = n/1
n %= 1
nota050 = n/0.5
n %= 0.5
nota025 = n/0.25
n %= 0.25
nota010 = n/0.1
n %= 0.1
nota005 = n/0.05
n %= 0.05
nota001 = float('%.2f' % (n/0.01))

print '''NOTAS:
%d nota(s) de R$ 100.00
%d nota(s) de R$ 50.00
%d nota(s) de R$ 20.00
%d nota(s) de R$ 10.00
%d nota(s) de R$ 5.00
%d nota(s) de R$ 2.00
MOEDAS:
%d moeda(s) de R$ 1.00
%d moeda(s) de R$ 0.50
%d moeda(s) de R$ 0.25
%d moeda(s) de R$ 0.10
%d moeda(s) de R$ 0.05
%d moeda(s) de R$ 0.01''' %(nota100,nota50,nota20,nota10,nota5,nota2,nota1,nota050,nota025,nota010,nota005,round(nota001))
