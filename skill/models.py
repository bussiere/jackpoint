from django.db import models











class Skill(models.Model):

	Nom = models.CharField(max_length=200)

	Texte = models.CharField(max_length=1500)

	Tag = models.ManyToManyField('tag.Tag')

	FamilleTag= models.ManyToManyField('tag.FamilleTag')



class Group_skills(models.Model):

	Nom = models.CharField(max_length=200)

	Texte = models.CharField(max_length=1500)

	Skills = models.ManyToManyField(Skill)

	Tag = models.ManyToManyField('tag.Tag')

	FamilleTag= models.ManyToManyField('tag.FamilleTag')

