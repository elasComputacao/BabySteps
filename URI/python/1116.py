num = int(input())
for i in range(num):
    n = input().split()
    x,y = int(n[0]),int(n[1])
    if y == 0:
        print('divisao impossivel')
    else:
        div = x/y
        print('{:.1f}'.format(div))
