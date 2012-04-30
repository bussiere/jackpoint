from jackpoint.jack.models import CaracUser,SkillUser,ItemUser,UserProfile,NotificationUser
from jackpoint.hand.models import Question
from jackpoint.engine.models import Notification
from django.contrib.auth.models import User


#TODO
#A affiner si la personne peut repondre totalement a la question ou pas.
def sendnotification(question,ThreadEngine):
    skills = question.Skills.all()
    items = question.Items.all()
    caracs = question.Caracs.all()
    user = {}
    for skill in skills :
        jacks = UserProfile.objects.filter(Skills__icontains = skill)
        #TODO
        #A optimiser
        for jack in jacks :
            user[jack.id] = jack.id
    for item in items :
        jacks = UserProfile.objects.filter(Items__icontains = item)
        #TODO
        #A optimiser
        for jack in jacks :
            user[jack.id] = jack.id
    for carac in caracs :
        jacks = UserProfile.objects.filter(Caracs__icontains = carac)
        #TODO
        #A optimiser
        for jack in jacks :
            user[jack.id] = jack.id
    
    for id in user.keys() :
        u = User.objects.get(id=id)
        try :
            notification = Notification.objects.get(ThreadEngine=ThreadEngine)
        except :
            notification =  Notification.objects.create(ThreadEngine=ThreadEngine)
        notification.save()
        notificationuser = NotificationUser.objects.create(Notification=notification)
        notificationuser.save()
        u.get_profile().Notifications.add(notificationuser)
        u.get_profile().save()
        u.save()
        