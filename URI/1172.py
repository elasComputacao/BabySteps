vector = []

for index in range(10):

	value = int(input())

	if value<1:
		value = 1

	vector.append(value)

	print ("X[%d] = %d"%(index,vector[index]))
