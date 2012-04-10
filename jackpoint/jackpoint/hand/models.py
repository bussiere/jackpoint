from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Answer(models.Model):  
    user = models.OneToOneField(User, null=True, blank=True)  
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    Url = models.TextField(null=True, blank=True)

class Question(models.Model):  
    user = models.OneToOneField(User, null=True, blank=True)  
    #other fields here
    Skills = models.ManyToManyField("jack.SkillUser", null=True, blank=True)
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Items = models.ManyToManyField("item.Item", null=True, blank=True)
    Caracs = models.ManyToManyField("carac.Carac", null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    Url = models.TextField(null=True, blank=True)
