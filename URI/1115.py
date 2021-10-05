quadrantes = []

while True:
	x, y = input().split(" ")
	
	if int(x) == 0 or int(y) == 0: break

	if int(x) > 0 and int(y) > 0:
		quadrantes.append("primeiro")

	elif int(x) < 0 and int(y) > 0:
		quadrantes.append("segundo")
	
	elif int(x) < 0 and int(y) < 0:
		quadrantes.append("terceiro")
	
	else:
		quadrantes.append("quarto")

for i in quadrantes:
	print(i)
	