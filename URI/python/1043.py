#1043(com o map)
valores = input().split()
valores = list(map(float, valores))
a, b, c = valores


perimetro = a + b + c
trapezio = (a + b) * c / 2

if a + b > c and a + c > b and b + c > a:
    print(f"Perimetro = {perimetro:.1f}")
else:
    print(f"Area = {trapezio:.1f}")
