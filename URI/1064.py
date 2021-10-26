x = 0
m = 0
for i in range(6):
    n = float(input())
    if n > 0:
        x += 1
        m += n
print('{} valores positivos\n{:.1f}'.format(x,m/x))
