i = 0

tab = ["TypeTransport","LigneTransport","Transport"]




t=""
while i < 6 :
    i += 1
    for ti in tab :
        t += """        try:
            place['%s%i'] = request.POST['%s%i']
        except:
            pass\n"""%(ti,i,ti,i)

i = 0
while i < 6 :
    i += 1
    for ti in tab :
        t += """    place['%s%i']\n"""%(ti,i)
mon_fichier2 = open("result.txt", "w")
mon_fichier2.write(t)
mon_fichier2.close()