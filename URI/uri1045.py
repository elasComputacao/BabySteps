#uri 1045

a, b, c = map(float, input().split())
lista = [a, b, c]
lista.sort(reverse=True, key=float)
a, b, c = lista

if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:

    if a == (b**2 + c**2)**0.5:
        print("TRIANGULO RETANGULO")
    elif a > (b**2 + c**2)**0.5:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif (a==b) or (b==c):
        print("TRIANGULO ISOSCELES")