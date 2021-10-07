lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.sort()
soma = 0
for i in range ((lista[0]),lista[1]+1):
    if i % 13 != 0:
        soma += i

print(soma)
