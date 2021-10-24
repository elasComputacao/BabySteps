n = int(input())
x = n
x = []
inn = 0
out = 0
if(n < 10000):
    for num in range (0 , n):
        x.append(int(input()))
    for num in x:
        if(-10**7 < num and num < 10**7):
            if( num > 10):
                inn = 1+inn
            else:
               out = 1+out
        
    
print(inn, "in")
print(out, "out")
