while True:
    try:
        n, m = [int(v) for v in input().split()]
        rept = m - n
        cont = n
        lista = []
        for i in range(rept):
            lista.append(cont)
            cont +=1
        lista.append(m)
        cont = 0
        for b in range (len(lista)):
            num = str(lista[b])
            if (len(set(num))) != (len(num)):
                cont += 1
        print(len(lista) - cont)
    except EOFError:
        break
