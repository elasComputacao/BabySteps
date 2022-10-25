#Questão 2466 - Sinuca

while True:
    try:
        num_bolas = input()
        num_bolas = int(num_bolas)

        bolas = input().split()
        
        sinuca = {}
        for i in range(num_bolas-1, -1, -1):
            if(i == num_bolas-1):
                sinuca[i] = bolas
            else: sinuca[i] = []

        for fila in sinuca:
            if fila != (num_bolas -1):
                for bola in range(len(sinuca[fila+1])-1):
                    b1 = sinuca[fila+1][bola]
                    b2 = sinuca[fila+1][bola+1]
                    sinuca[fila].append(1 if b1 == b2 else -1) 
        
        if sinuca[0] == [-1]: print('branca')
        else: print('preta')

    except EOFError:
        break