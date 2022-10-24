entrada = int(input())
for i in range(entrada):
    num = int(input())
    soma = 0
    for j in range(1, num):
        if num % j == 0:
            soma += j

    if soma == num:
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")
