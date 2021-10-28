contador_i = 0
contador_j = 0
i = [1,3,5,7,9]
j = [7,6,5]
while True:
    if i[contador_i] == i[-1] and contador_j == 3: break

    if contador_j == 3:
        contador_j = 0
        contador_i += 1

    print(f"I={i[contador_i]} J={j[contador_j]}")
    contador_j += 1

