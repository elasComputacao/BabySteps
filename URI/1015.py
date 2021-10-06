p1 = input().split()
p2 = input().split()

x2x1 = float(p2[0]) - float(p1[0])
y2y1 = float(p2[1]) - float(p1[1])

distancia = ((x2x1**2) + (y2y1**2))**(1/2)



print("{:.4f}".format(distancia))
