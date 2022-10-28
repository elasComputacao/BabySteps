flag = True
sum = 0
cont = 0

while(flag):
  num = int(input())
  if(num < 0):
    flag = False
  else:
    sum += num
    cont += 1

media = sum / cont
print("{:.2f}".format(media))
