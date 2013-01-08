i = 0
t = ""
while i < 6 :
    i += 1
    t +="""    try :
            typetransport = TypeTransport.objects.get(Nom=place['TypeTransport%i'])
    except :
            typetransport = TypeTransport.objects.create(Nom=place['TypeTransport%i'])
            typetransport.save()
    try :
        ligne = Ligne.objects.get(TypeTransport=typetransport,Nom=place['LigneTransport%i'])
    except :   
        ligne =  Ligne.objects.create(TypeTransport=typetransport,Nom=place['LigneTransport%i'])
        ligne.save()
    try :
        station = Station.objects.get(Ligne__in=ligne,Nom=place['Transport%i'])
    except :
        station = Station.objects.create(Nom=place['Transport%i'])
        station.Ligne.add(ligne)
        station.save()
    Lieu.Station.add(station)\n"""%(i,i,i,i,i,i)

mon_fichier2 = open("result.txt", "w")
mon_fichier2.write(t)
mon_fichier2.close()