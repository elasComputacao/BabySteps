contador = 0
i = [1,3,5,7,9]
j = 7
indice_i = 0
while True:
    print(f"I={i[indice_i]} J={j}")
    contador += 1
    j -= 1
    
    if i[indice_i] == i[-1]:
        if contador == 3:
            break
    
    if contador == 3:
        indice_i += 1
        contador = 0
        j += 5