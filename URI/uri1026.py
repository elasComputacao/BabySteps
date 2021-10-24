#uri 1026

lista = []
while True:
    try:
        line = input().split()
        lista.append(line)
    except EOFError:
        break

for n in lista:
    num1, num2 = int(bin(int(n[0])).split("b")[1]), int(bin(int(n[1])).split("b")[1])
    x = str(num1 + num2).replace("2", "0")
    num, i = 0, 0
    for n in range(-1, -len(x)-1, -1):
        num += int(x[n]) * (2**i)
        i += 1
    print(num)