import os
import re



def listing(path=".",regexp=""):
    list = []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            print os.path.join(dirname, subdirname)
        for filename in filenames:
            file = os.path.join(dirname, filename)
            if  re.search(regexp,file) :
                list.append(file)
    return list


def remplacementfichier(file=""):
    source = open(file, "r")
    final = []
    nomfile = file.split("\\")[1]
    nomfile = nomfile[0].capitalize() + nomfile[1:]
    for ligne in source.readlines():
        
##        if  re.search(".*class.*",ligne) :
##            classe = ligne.replace("class","").replace("(models.Model):","").replace(" ","")
##            print classe
##            classe2 = nomfile+"_"+classe
##            print classe2
##            ligne = ligne.replace(classe,classe2)
##            print ligne
##            
##        if  re.search(".*models.ManyToManyField.*",ligne)and (not re.search(".*related_name.*",ligne)):
##            champs = ligne.split("=")[0].replace(" ","")
##            extern = ligne.split("(")[1].replace("'","").replace(".","_").split(",")[0]
##            print ligne
##            ligne = ligne.replace("',","',related_name='"+classe2+"_"+champs+"',")
##            print ligne
##        ligne = ligne.replace("\.Liens","\.Lien")
        final.append(ligne)
    source.close()
    final.append("""\r\nclass Admin:\r\n    pass""")
    source = open(file, "w")
    for ligne in final :
        source.write(ligne+"\n")
    source.close()

list = listing(regexp=".*models.py$")

for file in list :
    print file
    remplacementfichier(file)
    

            
