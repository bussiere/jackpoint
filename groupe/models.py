from django.db import models







class Date_Visite(models.Model):



    Date = models.DateTimeField('Datee.date');







class Groupe(models.Model):



    Jugement = models.ManyToManyField('jugement.Jugement',related_name='Groupe_Jugement_jugement_Jugement',null=True,blank=True)



    PoigneeMain = models.ManyToManyField('poigneemain.Poignee',related_name='Groupe_PoigneeMain_poigneemain_PoigneeMain',null=True,blank=True)



    Kharma = models.ManyToManyField('kharma.Kharma',related_name='Groupe_Kharma_kharma_Kharma',null=True,blank=True)



    Importance = models.ManyToManyField('importance.Importance',related_name='Groupe_Importance_importance_Importance',null=True,blank=True)



    Liens =  models.ManyToManyField('lien.Lien',related_name='Groupe_Liens_liens_Liens',null=True,blank=True)



    LienFacebook =  models.ManyToManyField('lien.LienFacebook',related_name='Groupe_LienFacebook_liens_LienFacebook',null=True,blank=True)



    LienTwitter =  models.ManyToManyField('lien.LienTwitter',related_name='Groupe_LienTwitter_liens_LienTwitter',null=True,blank=True)



    Membre = models.ManyToManyField('membre.Membre')



    Nom = models.CharField(max_length=300)



    Date_creation = models.DateTimeField('date inscription',null=True,blank=True)



    Naissance = models.DateTimeField('Date de naissance',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Groupe_Tag_tag_Tag',null=True,blank=True)



    IP = models.ManyToManyField('ip.IP',related_name='Groupe_IP_ip_IP',null=True,blank=True)



    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Groupe_Note_divers_note_Note_divers',null=True,blank=True)



    Referer = models.CharField(max_length=1500,null=True,blank=True)



    Langue = models.ManyToManyField('langue.Langue',related_name='Groupe_Langue_langue_Langue',null=True,blank=True)



    Date_Visite = models.ManyToManyField(Date_Visite,null=True,blank=True)



    Abo_Newsletter = models.BooleanField()



    Skills = models.ManyToManyField('skill.Skill',related_name='Groupe_Skills_skills_Skills)',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Groupe_Lieux_lieux_Lieux)',null=True,blank=True)



    Fiche = models.ManyToManyField('fiche.Fiche',null=True,blank=True)



    Gallery = models.ManyToManyField('gallerie.Gallerie',null=True,blank=True)



    Reputation = models.ManyToManyField('reputation.Reputation',related_name='Groupe_Reputation_reputation_Reputation',null=True,blank=True)











class GroupeAmis(models.Model):



     Groupeself = models.ManyToManyField(Groupe,related_name='Groupe_self',null=True,blank=True)



     GroupesAmis = models.ManyToManyField(Groupe,related_name='Groupe_amis',null=True,blank=True)



    







# Create your models here.




class Admin:
    pass
