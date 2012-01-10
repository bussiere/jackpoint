from django.db import models







# Create your models here.



class CategorieTexte(models.Model):



    Nom = models.CharField(max_length=250)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Visibilite_CategorieTexte',null=True,blank=True)







class Entete(models.Model):



    Texte = models.CharField(max_length=400)







class Texte_Article(models.Model):



    CategorieTexte = models.ManyToManyField(CategorieTexte,null=True,blank=True)



    Texte = models.CharField(max_length=100000)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Visibilite_Texte_Article',null=True,blank=True)



    Image = models.ManyToManyField('image.Image',related_name='Image_Texte_Article',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Lieux_Texte_Article',null=True,blank=True)



    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='Evenement_Texte_Article',null=True,blank=True)



    Date = models.ManyToManyField('date.Date',related_name='Date_Texte_Article',null=True,blank=True)



    Info = models.ManyToManyField('info.Info',related_name='Info_Texte_Article',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Article_Tag_Texte_Article',null=True,blank=True)



    Lien = models.ManyToManyField('lien.Lien',related_name='Lien_Texte_Article',null=True,blank=True)



    LienFacebook = models.ManyToManyField('lien.LienFacebook',related_name='LienFacebook_Texte_Article',null=True,blank=True)



    LienTwitter = models.ManyToManyField('lien.LienTwitter',related_name='LienTwitter_Texte_Article',null=True,blank=True)



    







class Article(models.Model):



    Texte = models.ManyToManyField(Texte_Article,null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Article_Tag',null=True,blank=True)



    Membre = models.ManyToManyField('membre.Membre',related_name='Membre_Texte_Article',null=True,blank=True)



    Groupe = models.ManyToManyField('groupe.Groupe',related_name='Groupe_Texte_Article',null=True,blank=True)



    GroupeReco = models.ManyToManyField('groupe.Groupe',related_name='GroupeReco_Texte_Article',null=True,blank=True)



    MembreReco = models.ManyToManyField('membre.Membre',related_name='MembreReco_Texte_Article',null=True,blank=True)



    Notation = models.ManyToManyField('notation.Notation',related_name='Notation_Texte_Article',null=True,blank=True)



    Skills = models.ManyToManyField('skill.Skill',related_name='Skills_Texte_Article',null=True,blank=True)



    MembreCreateur =  models.ManyToManyField('membre.Membre',related_name='MembreCreateur_Texte_Article',null=True,blank=True)



    GroupeCreateur = models.ManyToManyField('groupe.Groupe',related_name='GroupeCreateur_Texte_Article',null=True,blank=True)


class Admin:
    pass
