from django.db import models
Jour = (
    (0, 'None'),
    (1, 'Lundi'),
    (2, 'Mardi'),
    (3, 'Mercredi'),
    (4, 'Jeudi'),
    (5, 'Vendredi'),
    (6, 'Samedi'),
    (7, 'Dimanche'),
)


Minute = (
         (0, '00'),
(1, '01'),
(2, '02'),
(3, '03'),
(4, '04'),
(5, '05'),
(6, '06'),
(7, '07'),
(8, '08'),
(9, '09'),
(10, '10'),
(11, '11'),
(12, '12'),
(13, '13'),
(14, '14'),
(15, '15'),
(16, '16'),
(17, '17'),
(18, '18'),
(19, '19'),
(20, '20'),
(21, '21'),
(22, '22'),
(23, '23'),
(24, '24'),
(25, '25'),
(26, '26'),
(27, '27'),
(28, '28'),
(29, '29'),
(30, '30'),
(31, '31'),
(32, '32'),
(33, '33'),
(34, '34'),
(35, '35'),
(36, '36'),
(37, '37'),
(38, '38'),
(39, '39'),
(40, '40'),
(41, '41'),
(42, '42'),
(43, '43'),
(44, '44'),
(45, '45'),
(46, '46'),
(47, '47'),
(48, '48'),
(49, '49'),
(50, '50'),
(51, '51'),
(52, '52'),
(53, '53'),
(54, '54'),
(55, '55'),
(56, '56'),
(57, '57'),
(58, '58'),
(59, '59'),
(60, '60')
         )
Heure = (
         (0, '00'),
(1, '01'),
(2, '02'),
(3, '03'),
(4, '04'),
(5, '05'),
(6, '06'),
(7, '07'),
(8, '08'),
(9, '09'),
(10, '10'),
(11, '11'),
(12, '12'),
(13, '13'),
(14, '14'),
(15, '15'),
(16, '16'),
(17, '17'),
(18, '18'),
(19, '19'),
(20, '20'),
(21, '21'),
(22, '22'),
(23, '23'),
(24, '24'),
)

class Plage(models.Model):
    DebutH = models.IntegerField(choices=Heure)
    DebutM = models.IntegerField(choices=Minute)
    FinH = models.IntegerField(choices=Heure)
    FinM = models.IntegerField(choices=Minute)
    def __unicode__(self):
        return str("%d:%d ~ %d:%d"%(self.DebutH,self.DebutM,self.FinH,self.FinM))



class Jour(models.Model):
    Jour = models.IntegerField(choices=Jour)
    
    def __unicode__(self):
        return str("%d %s"%(self.Jour,self.Horaire))

class Horaire(models.Model):
    Horaire = models.ManyToManyField("Plage", null=True, blank=True)
    def __unicode__(self):
        return str("%s"%(self.Jours))

    
class DateJourHoraire(models.Model):
    Date = models.DateField(null=True, blank=True)
    Jour = models.ForeignKey('Jour')
    Horaire = models.ManyToManyField("Plage", null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.Date + " " + self.Jour)
    
    
