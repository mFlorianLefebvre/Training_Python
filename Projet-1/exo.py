name = input("entrez un nom: ")
opening_file = open("data.txt")
It_is_here = True
for line in opening_file:
	words = line.split()
	age = words [1]
	if name == words[0]:
		print(words[1])
	else:
		It_is_here = False