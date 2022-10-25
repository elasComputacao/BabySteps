#leitura dos valores da entrada
valores = list(map(int,input().split()))

#cópia dos valores
listaOrdenada = valores[:]

#ordenar os valores
listaOrdenada.sort()

#saída dos valores em ordem crescente
for i in listaOrdenada:
    print(i)
print()
#saída dos valores na ordem que foram inseridos
for c in valores:
    print(c)