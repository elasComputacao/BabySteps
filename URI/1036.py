# Fórmula de Bhaskara

[a, b, c] = [float(i) for i in input().split()]

delta = (b ** 2) - 4 * a * c

if a == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    x1 = round((-b + delta ** (1 / 2)) / (2 * a), 5)
    x2 = round((-b - delta ** (1 / 2)) / (2 * a), 5)

    print("R1 = {}\nR2 = {}".format(x1, x2))
