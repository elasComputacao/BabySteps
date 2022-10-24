l = input().split(" ")
A = int(l[0])
B = int(l[1])


if A % B == 0 or B % A == 0:
     print("Sao Multiplos")
else:
     print("Nao sao Multiplos")
