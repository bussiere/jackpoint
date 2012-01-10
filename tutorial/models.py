from django.db import models







from django.db import models







# Create your models here.



class CategorieTexte(models.Model):



    Nom = models.CharField(max_length=250)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Tutorial_categorietexte_visibilite',null=True,blank=True)







class Entete(models.Model):



    Texte = models.CharField(max_length=400)







class Texte(models.Model):



    CategorieTexte = models.ManyToManyField(CategorieTexte,null=True,blank=True)



    Texte = models.CharField(max_length=100000)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Tutorial_Texte_Visibilite_Visibilite_visibilite',null=True,blank=True)



    Image = models.ManyToManyField('image.Image',related_name='Tutorial_Texte_Image_image_image',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Tutorial_Texte_Lieux_lieux_Lieux',null=True,blank=True)



    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='Tutorial_Texte_Evenement_evenement_Evenement',null=True,blank=True)



    Date = models.ManyToManyField('date.Date',related_name='Tutorial_Texte_Date_date_Date',null=True,blank=True)



    Info = models.ManyToManyField('info.Info',related_name='Tutorial_Texte_Info_info_Info',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Tutorial_Texte_Tag_tag_Tags',null=True,blank=True)



    Lien = models.ManyToManyField('lien.Lien',related_name='Tutorial_Texte_Lien_lien_Liens',null=True,blank=True)



    LienFacebook = models.ManyToManyField('lien.LienFacebook',related_name='Tutorial_Texte_LienFacebook_lien_LienFacebook',null=True,blank=True)



    LienFacebook = models.ManyToManyField('lien.LienTwitter',related_name='Tutorial_Texte_LienFacebook_lien_LienTwitter',null=True,blank=True)



    







class Tutorial(models.Model):



    Texte = models.ManyToManyField(Texte,null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Tutorial_Tag_tag_Tags',null=True,blank=True)



    membre = models.ManyToManyField('membre.Membre',related_name='Tutorial_membre_membre_Membre',null=True,blank=True)



    Groupe = models.ManyToManyField('groupe.Groupe',related_name='Tutorial_Groupe_groupe_Groupe',null=True,blank=True)



    GroupeReco = models.ManyToManyField('groupe.Groupe',related_name='Tutorial_GroupeReco_groupe_Groupe',null=True,blank=True)



    membreReco = models.ManyToManyField('membre.Membre',related_name='Tutorial_membreReco_membre_Membre',null=True,blank=True)



    Notation = models.ManyToManyField('notation.Notation',related_name='Tutorial_Notation_notation_notation',null=True,blank=True)



    Skills = models.ManyToManyField('skill.Skill',related_name='Tutorial_Skills_skills_Skills',null=True,blank=True)



    Skills = models.ManyToManyField('skill.Skill',related_name='Tutorial_Skills_skills_Skills',null=True,blank=True)



    MembreCreateur =  models.ManyToManyField('membre.Membre',related_name='Tutorial_MembreCreateur_membre_Membre',null=True,blank=True)



    GroupeCreateur = models.ManyToManyField('groupe.Groupe',related_name='Tutorial_GroupeCreateur_groupe_Groupe',null=True,blank=True)


class Admin:
    pass
