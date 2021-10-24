#uri 1131

g, i, e = 0, 0, 0
while True:
    x = list(map(int, input().split()))
    if x[0]==x[1]:
        e += 1
    elif x[0]>x[1]:
        i += 1
    else:
        g += 1
    x = int(input("Novo grenal (1-sim 2-nao)"))
    if x==2:
        break

print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(g+e+i, i, g, e))
if g==i:
    print("Nao houve vencedor")
elif g>i:
    print("Gremio venceu mais")
else:
    print("Inter venceu mais")
