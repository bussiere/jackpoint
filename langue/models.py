from django.db import models







# Create your models here.



class Langue(models.Model):



        Abr = models.CharField(max_length=3)

        Nom = models.CharField(max_length=25)



        Note_divers = models.ManyToManyField('note.Note_divers',related_name='Langue_Note_divers_notes_Note_divers',null=True,blank=True)



	




class Admin:
    pass
