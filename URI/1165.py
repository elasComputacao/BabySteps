n = int(input())
for i in range(n):
    num = int(input())
    lista = []
    for valor in range(1, num +1):
        if num % valor == 0:
            lista.append(valor)

    if lista == [1, num]:
        print(f"{num} eh primo")
    else:
        print(f"{num} nao eh primo")