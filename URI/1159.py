

while True:

	soma = 0
	index = 0

	x = int(input())

	if x==0:
		break

	while True:

		if x%2!=0:
			x += 1

		soma += x + index

		index += 2

		if index==10:
			break


	print (soma)

