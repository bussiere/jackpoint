from django.db import models



# Create your models here.





class Categorie_Page(models.Model):

	Nom  = models.CharField(max_length=200,blank=True)

	Note_divers = models.ManyToManyField('note.Note_divers',related_name='pages_Categorie_Page_Note_divers_notes_Note_divers',blank=True)



class Template(models.Model):

	Nom =  models.CharField(max_length=200,blank=True)

	contenu = models. TextField(max_length=80000,blank=True)

	Note_divers = models.ManyToManyField('note.Note_divers',related_name='Template_Note_divers_notes_Note_divers',blank=True)

	

class Page(models.Model):

    Template = models.ManyToManyField(Template,null=True,blank=True)

    self_url = models.ManyToManyField('lien.Lien',related_name='pages_lien_self',null=True,blank=True)

    Categorie = models.ManyToManyField(Categorie_Page,null=True,blank=True)

    Liens = models.ManyToManyField('lien.Lien',related_name="Liens sur la page",null=True,blank=True)

    Nom = models.CharField(max_length=200)

    ImagesSite = models.ManyToManyField('presentation.ImageSite',related_name='ImagesSite_presentation_ImageSite',null=True,blank=True)

    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',related_name='Texte_contenu_presentation_Texte_contenu',null=True,blank=True)

    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Note_divers_notes_Note_divers',null=True,blank=True)	

    MiseEnForme = models.ManyToManyField('presentation.MiseEnForme',related_name='MiseEnForme_presentation_MiseEnForme',null=True,blank=True)

    Menu = models.ManyToManyField('presentation.Menu',related_name='Menu_presentation_Menu',null=True,blank=True)

    Notation = models.ManyToManyField('notation.Notation',related_name='Avis_moteur_Avis',null=True,blank=True)

    Regle = models.ManyToManyField('regles.Regle',related_name='Regle_regles_Regle',null=True,blank=True)

    generated = models.DateTimeField('date published',blank=True,null=True)

    modified = models.DateTimeField('date modified',blank=True,null=True)

    protege = models.BooleanField(blank=True)

