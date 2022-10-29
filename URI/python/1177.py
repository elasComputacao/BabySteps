T=int(input())
N=[]
cont=0
if 2<= T <= 50:
    while cont <= 1000:
        for i in range(T):
            N.append(i)
            cont+=1
for a in range(1000):
    print("N[%d] = %d" %(a,N[a]))
