from django.db import models



# Create your models here.

#a combien de poignee de main du fondateur

class Poignee(models.Model):

    Nombre = models.FloatField(max_length=1000)
