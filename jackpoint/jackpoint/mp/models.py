from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MP(models.Model):  
    Texte = models.TextField(max_length=5012, null=True, blank=True)
    Sender = models.ForeignKey(User, unique=False, null=True, blank=True,related_name="Sender") 
    Receiver = models.ForeignKey(User, unique=False, null=True, blank=True,related_name="Receiver") 
    Seen = models.BooleanField(default=False)