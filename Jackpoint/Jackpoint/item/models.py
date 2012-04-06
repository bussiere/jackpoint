from django.db import models

# Create your models here.
class Item(models.Model):  
    Name = models.CharField(max_length=128)
    Skills = models.ManyToManyField("skill.Skill")