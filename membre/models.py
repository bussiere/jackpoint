from django.db import models



from django.contrib.auth.models import User



from jackpoint.presentation.models import Langue



















class Date_Visite(models.Model):



    Date = models.DateTimeField('Date visite')







class Site_hack_css(models.Model):



	Site = models.URLField()







class Anonymous(models.Model):



    Referer = models.CharField(max_length=1500)



    Langue = models.ManyToManyField(Langue)



    IP = models.ManyToManyField('ip.IP')



    Date_Visite = models.ManyToManyField(Date_Visite,null=True,blank=True)











class Signature(models.Model):



    Texte = models.CharField(max_length=450)



    





class Skill_user(models.Model):
    NIVEAU = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)
    
    Skills = models.ManyToManyField('skill.Skill',related_name='Membre_Skills_skills_Skills)',null=True,blank=True)
    Niveau = models.IntegerField(max_length=2, choices=Niveau)

	



class Membre(models.Model):



    User = models.ForeignKey(User, unique=True) 



    Nom = models.CharField(max_length=200)



    Prenom = models.CharField(max_length=200)



    Email =  models.ManyToManyField('contact.Email',related_name='Membre_Email_contact_Email',null=True,blank=True)



    Tel = models.ManyToManyField('contact.Telephone',related_name='Membre_Tel_contact_Telephone',null=True,blank=True)



    Date_inscription = models.DateTimeField('date inscription',null=True,blank=True)



    Naissance = models.DateTimeField('Date de naissance',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Membre_Tag_tag_Tag',null=True,blank=True)



    IP = models.ManyToManyField('ip.IP',related_name='Membre_IP_ip_IP',null=True,blank=True)



    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Membre_Note_divers_note_Note_divers',null=True,blank=True)



    Referer = models.CharField(max_length=1500,null=True,blank=True)



    Langue = models.ManyToManyField(Langue,null=True,blank=True)



    Date_Visite = models.ManyToManyField(Date_Visite,null=True,blank=True)



    Abo_Newsletter = models.BooleanField()



    Was_Anonymous = models.ManyToManyField('anonymous.Anonymous')



    Categorie = models.ManyToManyField('configurationsite.Categorie_Membre',related_name='Membre_Categorie_configuration_Categorie_Membre',null=True,blank=True)



    Historique_hack_css = models.ManyToManyField(Site_hack_css,null=True,blank=True)



    Skills = models.ManyToManyField('Skill_user',related_name='Membre_Skills_skills_Skills)',null=True,blank=True)    



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Membre_Lieux_lieux_Lieux)',null=True,blank=True)



    Fiche = models.ManyToManyField('fiche.Fiche',null=True,blank=True)



    Gallery = models.ManyToManyField('gallerie.Gallerie',null=True,blank=True)



    Liens =  models.ManyToManyField('lien.Lien',related_name='Membre_Liens_liens_Liens',null=True,blank=True)



    LienFacebook =  models.ManyToManyField('lien.LienFacebook',related_name='Membre_LienFacebook_liens_LienFacebook',null=True,blank=True)



    LienTwitter =  models.ManyToManyField('lien.LienTwitter',related_name='Membre_LienTwitter_liens_LienTwitter',null=True,blank=True)



    Signature = models.ManyToManyField(Signature)



    Jugement = models.ManyToManyField('jugement.Jugement',related_name='Membre_Jugement_jugement_Jugement',null=True,blank=True)



    PoigneeMain = models.ManyToManyField('poigneemain.Poignee',related_name='Membre_PoigneeMain_poigneemain_PoigneeMain',null=True,blank=True)



    Kharma = models.ManyToManyField('kharma.Kharma',related_name='Membre_Kharma_kharma_Kharma',null=True,blank=True)



    Importance = models.ManyToManyField('importance.Importance',related_name='Membre_Importance_importance_Importance',null=True,blank=True)



    Reputation = models.ManyToManyField('reputation.Reputation',related_name='Membre_Reputation_reputation_Reputation',null=True,blank=True)











class liste(models.Model):



    Membre = models.ManyToManyField('membre.Membre',null=True,blank=True)



    Amis = models.ManyToManyField('membre.Membre',related_name='Membre_Amis_membre_Membre',null=True,blank=True)



	



class Admin:
    pass
