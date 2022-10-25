par = 0

for i in range(5):

    n = int(input())

    if n % 2 == 0:
        par += 1

print(f'{par} valores pares')  