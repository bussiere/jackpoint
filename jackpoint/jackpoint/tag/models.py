from django.db import models

# Create your models here.
class Tag(models.Model):  
    Name = models.CharField(max_length=128,blank=True, null=True)