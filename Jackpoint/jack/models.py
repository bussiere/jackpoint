
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    Skills = models.ManyToManyField("skill.Skill")
    Tags = models.ManyToManyField("tag.Tag")
    Items = models.ManyToManyField("item.Items")
    Caracs = models.ManyToManyField("carac.Carac")
    Bio = models.TextField()
    Email = models.EmailField()
    Avatar = models.ImageField()

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 
