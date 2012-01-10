from django.db import models











class Date_Visite(models.Model):



    Date = models.DateTimeField('Date visite')







class Cookie(models.Model):



    IP = models.ManyToManyField('ip.IP')



    Date_Creation = models.DateTimeField('date creation')



    Date_Visite = models.ManyToManyField(Date_Visite)



    Historique_hack_css = models.ManyToManyField('membre.Site_hack_css')




class Admin:
    pass
