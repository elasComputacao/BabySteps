op = input().upper()
M = []
aux = []

for i in range(12):
    for j in range(12):
        aux.append(float(input()))
    M.append(aux)
    aux = []
        
sum = 0
count = 0
result = 0
for i in range(len(M)):
    for j in range(len(M[0])):
        if (j < i and j > (len(M) - i - 1)):
            sum += M[i][j]
            count += 1

if (op == "S"):
    result = sum
else:
    result = sum / count
    
print(f"{result:.1f}")