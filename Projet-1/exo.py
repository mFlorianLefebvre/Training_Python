name = raw_input("entrez un nom: ")
opening_file = open("data.txt", "r+")
it_is_here = False
for line in opening_file:
	words = line.split()
	age = words [1]
	if len(words) == 2 and name == words[0]:
		it_is_here = True
		print(words[1])
if it_is_here == False:
	age = raw_input("quel son age: ")
	opening_file.write("\n" + name + " " + age)