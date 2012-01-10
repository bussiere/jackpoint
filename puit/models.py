from django.db import models







# Create your models here.







class DocPuit(models.Model):



    Nom = models.CharField(max_length=200)



    Base64 = models.CharField(max_length=10000000)



    Dest = models.ManyToManyField('membre.Membre')



    Liens =  models.ManyToManyField('lien.Lien',related_name='DocPuit_Liens_liens_Liens',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='DocPuit_Tag_tag_Tag',null=True,blank=True)



    Skills = models.ManyToManyField('skill.Skill',related_name='DocPuit_Skills_skills_Skills',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='DocPuit_Lieux_lieux_Lieux',null=True,blank=True)



    Emails = models.ManyToManyField('contact.Email',related_name='DocPuit_Emails_Contact_Email',null=True,blank=True)



    







class Condition(models.Model):



    DocPuit = models.ManyToManyField(DocPuit,null=True,blank=True)



    Nom = models.CharField(max_length=200)



    Base64 = models.CharField(max_length=10000000)



    Dest = models.ManyToManyField('membre.Membre')



    Liens =  models.ManyToManyField('lien.Lien',related_name='Condition_Liens_liens_Liens',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Condition_Tag_tag_Tag',null=True,blank=True)



    Skills = models.ManyToManyField('skill.Skill',related_name='Condition_Skills_skills_Skills',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Condition_Lieux_lieux_Lieux',null=True,blank=True)



    Emails = models.ManyToManyField('contact.Email',related_name='Condition_Emails_Contact_Email',null=True,blank=True)



    

class Admin:
    pass
