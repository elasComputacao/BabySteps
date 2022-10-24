# Questão 1071 em Python

num1 = int(input())
num2 = int(input())
sum = 0

for num in range(num1 - 1, num2, -1):
    if (num % 2 == 1):
        sum += num

print(sum)