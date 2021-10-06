peca1 = input().split()
peca2 = input().split()

quantidadePeca1 = int(peca1[1])
quantidadePeca2 = int(peca2[1])
valorPeca1 = float(peca1[2])
valorPeca2 = float(peca2[2])

total = (quantidadePeca1 * valorPeca1) + (quantidadePeca2 * valorPeca2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
