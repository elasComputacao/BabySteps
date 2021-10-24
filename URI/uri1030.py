#uri 1030

num_casos = int(input())
lista_casos = []
for y in range(num_casos):
    line = input().split()
    lista_casos.append(line)

def myfunc(lista):
    n, k = map(int, lista)
    i = 1
    for x in range(1, n+1):
        y = (i + k-1)%x +1
        i = y
    return y

for line in lista_casos:
    resposta = myfunc(line)
    print("Case {}: {}".format((lista_casos.index(line)+1), resposta))