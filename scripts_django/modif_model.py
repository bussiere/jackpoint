import os
chemin = "/home/bussiere/Dropbox/Projets/jackpoint/jackpoint"

#(,
#(models.Model)
#(null=True,blank=True)
#models.NullBooleanField(blank=True)
#models.BooleanField(null=True,blank=True)
def flistemodel(chemin):
	listfile =  os.listdir(chemin) 
	listemodel = []
	for f in listfile :
		if os.path.isdir(os.path.join(chemin, f)):
			listindir =  os.listdir(os.path.join(chemin, f)) 
			for f2 in listindir :
				if f2 == "models.py":
					listemodel.append(os.path.join(chemin, f,f2))
	return listemodel


def replacemodel(ligne):
	ligne = ligne.replace(")",",null=True,blank=True)")
	ligne = ligne.replace("models.Model,null=True,blank=True","models.Model")
	ligne = ligne.replace("(,","(")
	ligne = ligne.replace("self,null=True,blank=True","self")
	ligne = ligne.replace("models.BooleanField(null=True,blank=True)","models.NullBooleanField(blank=True)")
    ligne = ligne.replace("models.BooleanField(null=True,blank=True)","models.NullBooleanField(blank=True)")
    ligne = ligne.replace("null=True,blank=True,null=True,blank=True","null=True,blank=True")
    return ligne

listemodel = flistemodel(chemin)
for m in listemodel :
	f = open(m, 'w')
	texte = f.read()
	texte = replacemodel(texte)
	f.write(texte)
	f.close()