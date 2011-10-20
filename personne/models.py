from django.db import models



class Personne(models.Model):

    Nom = models.CharField(max_length=200)

    Prenom = models.CharField(max_length=200)

    Email =  models.EmailField()

    Telephone = models.CharField(max_length=200,null=True,blank=True)

    Portable = models.CharField(max_length=200,null=True,blank=True)

    Date_inscription = models.DateTimeField('date inscription',null=True,blank=True)

    Naissance = models.DateTimeField('Date de naissance',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='Personne_Tag_tag_Tag',null=True,blank=True)

    IP = models.ManyToManyField('ip.IP',related_name='Personne_IP_ip_IP',null=True,blank=True)

    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Personne_Note_divers_note_Note_divers',null=True,blank=True)

    Skills = models.ManyToManyField('skill.Skill',related_name='Personne_Skills_skills_Skills)',null=True,blank=True)

    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Personne_Lieux_lieux_Lieux)',null=True,blank=True)

    Fiche = models.ManyToManyField('fiche.Fiche')

    Gallery = models.ManyToManyField('gallerie.Gallerie')

    Liens =  models.ManyToManyField('lien.Lien')

    LienFacebook =  models.ManyToManyField('lien.LienFacebook')

    LienTwitter =  models.ManyToManyField('lien.LienTwitter')

    Jugement = models.ManyToManyField('jugement.Jugement',related_name='Personne_Jugement_jugement_Jugement',null=True,blank=True)

    Kharma = models.ManyToManyField('kharma.Kharma',related_name='Personne_Kharma_kharma_Kharma',null=True,blank=True)

    Importance = models.ManyToManyField('importance.Importance',related_name='Personne_Importance_importance_Importance',null=True,blank=True)

    Reputation = models.ManyToManyField('reputation.Reputation',related_name='Personne_Reputation_reputation_Reputation',null=True,blank=True)

    MembreCreateur =  models.ManyToManyField('membre.Membre',related_name='Personne_MembreCreateur_membre_Membre',null=True,blank=True)

    GroupeCreateur = models.ManyToManyField('groupe.Groupe',related_name='Personne_GroupeCreateur_groupe_Groupe',null=True,blank=True)

# Create your models here.

