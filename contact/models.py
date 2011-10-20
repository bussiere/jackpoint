from django.db import models



# Create your models here.





class Telephone(models.Model):

    tel = models.CharField(max_length=200,null=True,blank=True)

    Principal = models.BooleanField()



class Email(models.Model):

    Email = models.EmailField()

    Principal = models.BooleanField()
