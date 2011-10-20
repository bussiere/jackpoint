from django.db import models



# Create your models here.





class Delicious(models.Model):

    Createur = models.ManyToManyField('membre.Membre',related_name='Delicious_Createur',null=True,blank=True)

    Dest = models.ManyToManyField('membre.Membre',related_name='Delicious_Dest',null=True,blank=True)

    Liens =  models.ManyToManyField('lien.Lien',related_name='Delicious_Liens_liens_Liens',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='Delicious_Tag_tag_Tag',null=True,blank=True)

    Skills = models.ManyToManyField('skill.Skill',related_name='Delicious_Skills_skills_Skill',null=True,blank=True)

    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Delicious_Lieux_lieux_Lieux',null=True,blank=True)
