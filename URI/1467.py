# Questão 1467 - Zerinho ou Um
while True:
    try:
        n = input().split()
        if n[0] == n[1] and n[1] == n[2]:
            print("*")
        elif n[0] == n[1] and n[1] != n[2]:
            print("C")
        elif n[1] == n[2] and n[1] != n[0]:
            print("A")
        elif n[2] == n[0] and n[2] != n[1]:
            print("B")
    except EOFError:
        break