n= int(input())

for i in range(0,n):
    num = int(input())
    j = 1
    s = 0
    while j < num:
        if num % j == 0:
            s = s + j
           
        j = j + 1
       
    if s == num:
        print('{} eh perfeito'.format(num))
    else:
        print('{} nao eh perfeito'.format(num))
