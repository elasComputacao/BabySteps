#Questão 2472 - Tapetes


import copy

while True:
    try:
        maior_soma = 0
        a, b = input().split()
        comp_tubo, num_tapetes = int(a), int(b)
        
        num_tapetes_aux = copy.deepcopy(num_tapetes)

        mais_alto = comp_tubo - num_tapetes + 1
        maior_soma += mais_alto
        num_tapetes_aux -= 1

        mais_altos = [mais_alto]

        for j in range((num_tapetes-1)):
            for i in range(mais_alto, -1, -1):
                aux = maior_soma + i
                if ((aux + num_tapetes_aux-1) <= comp_tubo) and aux <= comp_tubo:
                    mais_alto = i
                    mais_altos.append(mais_alto)
                    maior_soma = aux
                    num_tapetes_aux -= 1
                    break
        soma = 0
        for maior in mais_altos:
            soma += (maior* maior)
        
        print(soma)
        
    except EOFError:
        break