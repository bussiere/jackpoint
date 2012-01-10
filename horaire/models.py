from django.db import models







# Create your models here.



Minute = (



    (15, '15'),



    (30, '30'),



    (45, '45'),



    (00, '00'),



)



Heure = (



(0,'0h'),



(1,'1h'),



(2,'2h'),



(3,'3h'),



(4,'4h'),



(5,'5h'),



(6,'6h'),



(7,'7h'),



(8,'8h'),



(9,'9h'),



(10,'10h'),



(11,'11h'),



(12,'12h'),



(13,'13h'),



(14,'14h'),



(15,'15h'),



(16,'16h'),



(17,'17h'),



(18,'18h'),



(19,'19h'),



(20,'20h'),



(21,'21h'),



(22,'22h'),



(23,'23h'),



(24,'24h'),



)















class HoraireDebut(models.Model):



	 Minute = models.IntegerField(max_length=2, choices=Minute,blank=True)



	 Heure = models.IntegerField(max_length=2, choices=Heure,blank=True)







class HoraireFin(models.Model):



	 Minute = models.IntegerField(max_length=2, choices=Minute,blank=True)



	 Heure = models.IntegerField(max_length=2, choices=Heure,blank=True)







class Horaire(models.Model):



	HoraireDebut = models.ManyToManyField(HoraireDebut,null=True,blank=True)



	HoraireFin = models.ManyToManyField(HoraireFin,null=True,blank=True)







class Lundi(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Lundi_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Lundi_Note_notes_Note_divers',null=True,blank=True)







class Mardi(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Mardi_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Mardi_Note_notes_Note_divers',null=True,blank=True)



	



class Mercredi(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Mercredi_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Mercredi_Note_notes_Note_divers',null=True,blank=True)







class Jeudi(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Jeudi_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Jeudi_Note_notes_Note_divers',null=True,blank=True)







class Vendredi(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Vendredi_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Vendredi_Note_notes_Note_divers',null=True,blank=True)







class Samedi(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Samedi_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Samedi_Note_notes_Note_divers',null=True,blank=True)







class Dimanche(models.Model):



	HoraireDebut = models.ManyToManyField(Horaire,related_name='Dimanche_HoraireDebut_Horaire',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Dimanche_Note_notes_Note_divers',null=True,blank=True)







class Ouverture(models.Model):



	Lundi = models.ManyToManyField('Lundi',null=True,blank=True)



	Mardi = models.ManyToManyField('Mardi',null=True,blank=True)



	Mercredi = models.ManyToManyField('Mercredi',null=True,blank=True)



	Jeudi = models.ManyToManyField('Jeudi',null=True,blank=True)



	Vendredi = models.ManyToManyField('Vendredi',null=True,blank=True)



	Samedi = models.ManyToManyField('Samedi',null=True,blank=True)



	Dimanche = models.ManyToManyField('Dimanche',null=True,blank=True)



	Note = models.ManyToManyField('note.Note_divers',related_name='Ouverture_Note_notes_Note_divers',null=True,blank=True)



	Notation = models.ManyToManyField('note.Note_divers',related_name='Ouverture_Notation_notes_Note_divers',null=True,blank=True)


class Admin:
    pass
