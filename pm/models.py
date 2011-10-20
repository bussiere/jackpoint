from django.db import models





class PM(models.Model):

	Date = models.DateTimeField('Date visite')

	Sender = models.ManyToManyField('membre.Membre',related_name='member_sender',null=True,blank=True)

	SenderGroupe = models.ManyToManyField('groupe.Groupe',related_name='groupe_sender',null=True,blank=True)

	Dest = models.ManyToManyField('membre.Membre',related_name='member_dest',null=True,blank=True)

	DestGroupe = models.ManyToManyField('groupe.Groupe',related_name='groupe_dest',null=True,blank=True)

	Object = models.CharField(max_length=800)

	Texte = models.CharField(max_length=1500)





# Create your models here.

