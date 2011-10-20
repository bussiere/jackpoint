from django.db import models

class Evenement(models.Model):
    
    Date_Evenement = models.ManyToManyField('date.Date',related_name='Evenement_Date_Evenement',null=True,blank=True)
    
    Nom = models.CharField(max_length=200)

    Email =  models.ManyToManyField('contact.Email',related_name='Evenement_Email_contact_Email',null=True,blank=True)

    Tel = models.ManyToManyField('contact.Telephone',related_name='Evenement_Tel_contact_Telephone',null=True,blank=True)

    Date_inscription = models.DateTimeField('date inscription',null=True,blank=True)

    Naissance = models.DateTimeField('Date de naissance',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='Evenement_Tag_tag_Tag',null=True,blank=True)


    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Evenement_Note_divers_note_Note_divers',null=True,blank=True)

    Skills = models.ManyToManyField('skill.Skill',related_name='Evenement_Skills_skills_Skills)',null=True,blank=True)

    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Evenement_Lieux_lieux_Lieux)',null=True,blank=True)

    Fiche = models.ManyToManyField('fiche.Fiche',null=True,blank=True)

    Gallery = models.ManyToManyField('gallerie.Gallerie',null=True,blank=True)

    Liens =  models.ManyToManyField('lien.Lien',related_name='Evenement_Liens_liens_Liens',null=True,blank=True)

    LienFacebook =  models.ManyToManyField('lien.LienFacebook',related_name='Evenement_LienFacebook_liens_LienFacebook',null=True,blank=True)

    LienTwitter =  models.ManyToManyField('lien.LienTwitter',related_name='Evenement_LienTwitter_liens_LienTwitter',null=True,blank=True)

    Jugement = models.ManyToManyField('jugement.Jugement',related_name='Evenement_Jugement_jugement_Jugement',null=True,blank=True)

    Kharma = models.ManyToManyField('kharma.Kharma',related_name='Evenement_Kharma_kharma_Kharma',null=True,blank=True)

    Importance = models.ManyToManyField('importance.Importance',related_name='Evenement_Importance_importance_Importance',null=True,blank=True)

    Reputation = models.ManyToManyField('reputation.Reputation',related_name='Evenement_Reputation_reputation_Reputation',null=True,blank=True)

# Create your models here.

