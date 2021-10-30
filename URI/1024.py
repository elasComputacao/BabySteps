alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(raw_input())
for i in xrange(n):
	word = raw_input()
	aux_word = ""
	first_part = ""
	second_part = ""
	for j in xrange(len(word)-1, -1, -1):
		if(word[j].lower() in alpha):
			aux_word += chr(ord(word[j]) + 3)
		else:
			aux_word += word[j]
	middle = (len(word)/2)
	first_part = aux_word[0:middle]
	for k in xrange((len(aux_word)/2), len(aux_word)):
		second_part += chr(ord(aux_word[k]) -1)
	print first_part + second_part