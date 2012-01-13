from django.db import models



Type = (



    (1,'Root'),



    (2,'Admin'),



    (3, 'Membre'),







)



# Create your models here.



class Categorie_Membre (models.Model):



    Nom  = models.IntegerField(choices=Type,max_length=200,blank=True)



    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Categorie_Membre_Note_divers_notes_Note_divers',blank=True)







class Config_gallery(models.Model):
	Nombre_max_photos = models.IntegerField(blank=True,null=True)


class Admin:
    pass
