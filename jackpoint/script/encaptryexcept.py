mon_fichier = open("lit.txt", "r")
mon_fichier2 = open("result.txt", "w")
for line in mon_fichier.readlines() :
	line = line.replace("\r","")
	line = line.replace("\n","")
	line = "        try:\n            %s\n        except:\n            pass\n"%line
	mon_fichier2.write(line)

mon_fichier.close()
mon_fichier2.close()