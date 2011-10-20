from django.db import models



# Create your models here.

Visible = (

    (1, 'Root_aucun'),

    (2, 'Admin_Admin'),

    (3, 'Membre_Aucun'),

    (4, 'Membre_Amis'),

    (5, 'Membre_Amis_Amis'),

    (6, 'Tous')

)



class Visibilite(models.Model):

	 Visibilite = models.IntegerField(max_length=2, choices=Visible,blank=True)
