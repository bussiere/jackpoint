from django.db import models



# Create your models here.



class Texte(models.Model):

    Description = Texte = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True,related_name="moteur_Description Post")

    Texte = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True,related_name="moteur_Texte_Post")

    Langue = models.ManyToManyField('langue.Langue',related_name="moteur_langue",null=True,blank=True)

    Categorie = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True,related_name="moteur_Categorie")

    Note_divers = models.ManyToManyField('note.Note_divers',related_name="Moteur_note",null=True,blank=True)

    Skills = models.ManyToManyField('skill.Skill',related_name="moteur_skills",null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name="moteur_tag",null=True,blank=True)



class NiveauCategorie(models.Model):

    Niveau = models.CharField(max_length=10000)



class NiveauPost(models.Model):

    Niveau = models.CharField(max_length=10000)





class NiveauReponse(models.Model):

    Niveau = models.CharField(max_length=10000)





class Post(models.Model):

    Notation = models.ManyToManyField('notation.Notation',related_name="post_notation",null=True,blank=True)

    Membre = models.ManyToManyField('membre.Membre',related_name="post_membre",null=True,blank=True)

    Texte = models.ManyToManyField('Texte',null=True,blank=True)

    NiveauPost = models.ManyToManyField('NiveauPost',related_name="post_niveau",null=True,blank=True)

    NiveauReponse = models.ManyToManyField('NiveauPost',related_name="post_niveaureponse",null=True,blank=True)





class Reponse(models.Model):

    Post = models.ManyToManyField('Post',related_name="post_reponse",null=True,blank=True)

    Notation = models.ManyToManyField('notation.Notation',related_name="reponse_notation",null=True,blank=True)

    Membre = models.ManyToManyField('membre.Membre',related_name="reponse_membre",null=True,blank=True)

    Anonymous = models.ManyToManyField('anonymous.Anonymous',related_name="reponse_anonymous",null=True,blank=True)
    
    Texte = models.ManyToManyField('Texte',related_name="reponse_texte",null=True,blank=True)

    

