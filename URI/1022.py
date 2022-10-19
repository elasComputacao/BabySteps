def opera(n1, d1, op, n2, d2):
    if op == '+':
        num = (n1 * d2) + (n2 * d1)
        dem = d1 * d2
    elif op == '-':
        num = (n1 * d2) - (n2 * d1)
        dem = d1 * d2
    elif op == '*':
        num = n1 * n2
        dem = d1 * d2
    elif op == '/':
        num = n1 * d2
        dem = n2 * d1
    return num, dem


def fatora(a, b):
    abs_a, abs_b = abs(a), abs(b)
    menor = min(abs_a, abs_b)
    maior = max(abs_a, abs_b)
    divisor = menor
    while divisor > 1:
        if (menor % divisor) == 0:
            if (maior % divisor) == 0:
                return int(a/divisor), int(b/divisor)
        divisor -= 1
    return a, b


testes = int(input())
for teste in range(0, testes):
    operacoes = input().strip().split(' ')
    n1, d1, op, n2, d2 = int(operacoes[0]), int(operacoes[2]), operacoes[3], int(operacoes[4]), int(operacoes[6])
    num, dem = opera(n1, d1, op, n2, d2)
    simp_num, simp_dem = fatora(num, dem)
    print('{}/{} = {}/{}'.format(num, dem, simp_num, simp_dem))