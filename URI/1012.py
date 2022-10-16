#1012
valores = input().split(" ")

# a = float(valores[0])
# b = float(valores[1])
# c = float(valores[2])

triangulo = float(valores[0]) * float(valores[2]) / 2
circulo = 3.14159 * (float(valores[2])) ** 2
trapezio = (float(valores[0]) + float(valores[1])) * float(valores[2]) / 2
quadrado = float(valores[1]) ** 2
retangulo = float(valores[0]) * float(valores[1])

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
