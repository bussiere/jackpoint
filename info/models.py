from django.db import models











class CategorieTexte(models.Model):



    Nom = models.CharField(max_length=250)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Info_Categorie_Texte_Visibilite_Visibilite_visibilite',null=True,blank=True)







class Entete(models.Model):



    Texte = models.CharField(max_length=400)







class Texte(models.Model):



    CategorieTexte = models.ManyToManyField(CategorieTexte,null=True,blank=True)



    Texte = models.CharField(max_length=10000)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Info_Texte_Visibilite_Visibilite_visibilite',null=True,blank=True)



    Image = models.ManyToManyField('image.Image',related_name='Info_Texte_Image_image_image',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Info_Texte_Lieux_lieux_Lieux',null=True,blank=True)



    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='Info_Texte_Evenement_evenement_Evenement',null=True,blank=True)



    Date = models.ManyToManyField('date.Date',related_name='Info_Texte_Date_date_Date',null=True,blank=True)



    Info = models.ManyToManyField('info.Info',related_name='Info_Texte_Info_info_Info',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Info_Texte_Tag_tag_Tags',null=True,blank=True)



    Lien = models.ManyToManyField('lien.Lien',related_name='Info_Texte_Lien_lien_Liens',null=True,blank=True)



    Gallery = models.ManyToManyField('gallerie.Gallerie',null=True,blank=True)



    







   







class Info(models.Model):



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Info_Info_Lieux_lieux_Lieux)',null=True,blank=True)



    Fiche = models.ManyToManyField('fiche.Fiche',null=True,blank=True)



    Liens =  models.ManyToManyField('lien.Lien',related_name='Info_Info_Liens_liens_Liens',null=True,blank=True)



    LienFacebook =  models.ManyToManyField('lien.LienFacebook',related_name='Info_Info_LienFacebook_liens_LienFacebook',null=True,blank=True)



    LienTwitter =  models.ManyToManyField('lien.LienTwitter',related_name='Info_Info_LienTwitter_liens_LienTwitter',null=True,blank=True)



    Personne = models.ManyToManyField('personne.Personne',related_name='Info_Info_Personne_personne_Personne',null=True,blank=True)



    PersonneGroupe = models.ManyToManyField('personnegroupe.PersonneGroupe',related_name='Info_Info_PersonneGroupe_personnegroupe_PersonneGroupe',null=True,blank=True)



    Membrevise = models.ManyToManyField('membre.Membre',related_name='Info_Info_Membrevise_membre_Membre',null=True,blank=True)



    MembreCreateur = models.ManyToManyField('membre.Membre',related_name='Info_Info_MembreCreateur_membre_Membre',null=True,blank=True)



    Groupe = models.ManyToManyField('groupe.Groupe',related_name='Info_Info_Groupe_groupe_Groupe',null=True,blank=True)



    GroupeCreateur = models.ManyToManyField('groupe.Groupe',related_name='Info_Info_GroupeCreateur_groupe_Groupe',null=True,blank=True)



    GroupeReco = models.ManyToManyField('groupe.Groupe',related_name='Info_Info_GroupeReco_groupe_Groupe',null=True,blank=True)



    membreReco = models.ManyToManyField('membre.Membre',related_name='Info_Info_membreReco_membre_Membre',null=True,blank=True)



    Skills = models.ManyToManyField('skill.Skill',related_name='Info_Info_Skills_skills_Skills',null=True,blank=True)



    MembreCreateur =  models.ManyToManyField('membre.Membre',related_name='Info_Info_MembreCreateur_membre_Membre',null=True,blank=True)



    GroupeCreateur = models.ManyToManyField('groupe.Groupe',related_name='Info_Info_GroupeCreateur_groupe_Groupe',null=True,blank=True)



    



# Create your models here.




class Admin:
    pass
