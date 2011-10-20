from django.db import models





class CategorieTexte(models.Model):

	Nom = models.CharField(max_length=250)

	Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Fiche_Categorie_Texte_Visibilite_Visibilite_visibilite',null=True,blank=True)



class Entete(models.Model):

	Texte = models.CharField(max_length=400)



class Texte(models.Model):

	CategorieTexte = models.ManyToManyField(CategorieTexte,null=True,blank=True)

	Texte = models.CharField(max_length=10000)

	Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Fiche_Texte_Visibilite_Visibilite_visibilite',null=True,blank=True)

	Image = models.ManyToManyField('image.Image',related_name='Fiche_Texte_Image_image_image',null=True,blank=True)

	Lieux = models.ManyToManyField('lieux.Lieux',related_name='Fiche_Texte_Lieux_lieux_Lieux',null=True,blank=True)

	Evenement =  models.ManyToManyField('evenement.Evenement',related_name='Fiche_Texte_Evenement_evenement_Evenement',null=True,blank=True)

	Date = models.ManyToManyField('date.Date',related_name='Fiche_Texte_Date_date_Date',null=True,blank=True)

	Tag = models.ManyToManyField('tag.Tag',related_name='Fiche_Texte_Tag_tag_Tags',null=True,blank=True)

	Lien = models.ManyToManyField('lien.Lien',related_name='Fiche_Texte_Lien_lien_Liens',null=True,blank=True)



class Fiche(models.Model):

	Entete = models.ManyToManyField(Entete,null=True,blank=True)

	Texte = models.ManyToManyField(Texte,null=True,blank=True)

	Gallerie = models.ManyToManyField('gallerie.Gallerie',related_name='Fiche_Fiche_Gallerie_gallerie_Gallerie',null=True,blank=True)

	

	

	

	

class Update(models.Model):

	Texte = models.ManyToManyField(Texte,null=True,blank=True)

