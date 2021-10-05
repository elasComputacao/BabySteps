#Questão 2465 - passa a bolinha


def pega_proximo(matrix, lin, col):
    proxi = -1
    proxj = -1
    if matrix[lin][col]['p'] == 'N':
        proxi = lin
        proxj = col+1
        matrix[lin][col]['p'] = 'L'

    elif matrix[lin][col]['p'] == 'L':
        proxi = lin+1
        proxj = col
        matrix[lin][col]['p'] = 'S'

    elif matrix[lin][col]['p'] == 'S':
        proxi = lin
        proxj = col-1
        matrix[lin][col]['p'] = 'O'
    
    elif matrix[lin][col]['p'] == 'O':
        proxi = lin-1
        proxj = col
        matrix[lin][col]['p'] = 'N'

    return (proxi, proxj)


def recebe_bolinha(matrix, lin, col):
    matrix[lin][col]['b'] = 1
    for i in range(4):
        proxi, proxj = pega_proximo(matrix, lin, col)
        if proxi < len(matrix) and proxi >= 0 and proxj < len(matrix) and proxj >= 0:
            prox = matrix[proxi][proxj]['v']
            if prox >= matrix[lin][col]['v'] and matrix[proxi][proxj]['b'] == 0:
                recebe_bolinha(matrix, proxi, proxj)


while True:
    try:
        tam_matrix = input()
        tam_matrix = int(tam_matrix)
        lin, col = input().split()
        lin, col = int(lin), int(col)

        matrix = [ [ 0 for i in range(tam_matrix) ] for j in range(tam_matrix) ]

        for i in range(tam_matrix):
            linha = input().split()
            for j in range(tam_matrix):
                matrix[i][j] = {'v':linha[j], 'p': 'N', 'b': 0}

        recebe_bolinha(matrix, lin-1, col-1)

        num_bandeiras = 0

        for linha in range(tam_matrix):
            for coluna in range(tam_matrix):
                if matrix[linha][coluna]['b'] == 1:
                    num_bandeiras+=1

        print(num_bandeiras)
    except EOFError:
        break