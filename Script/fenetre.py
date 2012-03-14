string = ["totosdjfsdfsdfdsfsdfsdfsdfsdfsdft","titigsgsgsgsgsgsgs","tata"]

def encadrement(string,hauteur="#",largeurg="#",largeurd="#"):
	h = 0
	l = 0
	c = 0
	for t in string :
		if len(t) > l :
			l = len(t)
		h += 1
	rajout = l / 10
	if rajout == 0 :
		rajout = 1
	lignetop = ( l + rajout*4)*hauteur
	total = lignetop+"\n"
	for t in string :
		space = ((len(lignetop)-2-len(t))/2)
		if (space == 0 ):
			space = 1
		space1 = space
		space2 = space
		if len(largeurg+" "*space1+t+" "*space2+largeurd) < len(lignetop):
			space1 += 1
		total += largeurg+" "*space1+t+" "*space2+largeurd+"\n"
	total += lignetop+"\n"
	return total

print encadrement(string)
print encadrement(string,hauteur="*",largeurg="*",largeurd="*")
print encadrement(string,hauteur="/",largeurg="/",largeurd="/")
print encadrement(string,hauteur=";",largeurg=";",largeurd=";")
print encadrement(string,hauteur="_",largeurg="(",largeurd=")")