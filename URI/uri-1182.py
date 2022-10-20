def opera(coluna,operacao,M):
    soma = 0
    for i in range(12):
        soma += M[i][coluna]
    if operacao = "S":
        return soma
    return soma/12

def main():
    coluna = int(input())
    operacao = input()
    M = []
    for i in range(12):
        linha = []
        for j in range(12):
            x = float(input())
            linha.append(x)
        M.append(linha)
    print(opera(coluna,operacao,M))

main()
