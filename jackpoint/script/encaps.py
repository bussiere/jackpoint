Jour = {
    1:'Lundi',
    2:'Mardi',
    3:'Mercredi',
    4:'Jeudi',
    5:'Vendredi',
    6:'Samedi',
    7:'Dimanche',
}
mon_fichier2 = open("result.txt", "w")
M = ["M1","M11","M2","M22"]
AM = ["AM1","AM11","AM2","AM22"]
amm = [M,AM]
t = ""
for key in Jour.keys():
	print Jour[key]
	for m in amm :
		t +="""    try :
            result = Plage.objects.get(DebutH=place['%s%s'],DebutM= place['%s%s'],FinH=place['%s%s'], FinM=place['%s%s'])
    except :
            result = Plage.objects.create(DebutH=place['%s%s'],DebutM= place['%s%s'],FinH=place['%s%s'], FinM=place['%s%s'])
            result.save()
    plage.append(result)\n"""%(Jour[key],m[0],Jour[key],m[1],Jour[key],m[2],Jour[key],m[3],Jour[key],m[0],Jour[key],m[1],Jour[key],m[2],Jour[key],m[3])


mon_fichier2.write(t)

mon_fichier2.close()