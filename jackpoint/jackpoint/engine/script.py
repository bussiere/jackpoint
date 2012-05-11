from jackpoint.jack.models import CaracUser,SkillUser,ItemUser,UserProfile,NotificationUser
from jackpoint.hand.models import Question
from jackpoint.engine.models import Notification
from django.contrib.auth.models import User


#TODO
#A affiner si la personne peut repondre totalement a la question ou pas.
def sendnotification(question,threadEngine):
    skills = question.Skills.all()
    items = question.Items.all()
    caracs = question.Caracs.all()
    user = {}
    for skill in skills :
        jacks = UserProfile.objects.filter(Skills__id__icontains = skill.id)
        #TODO
        #A optimiser
        for jack in jacks :
            user[jack.id] = jack.id
    for item in items :
        jacks = UserProfile.objects.filter(Items__id__icontains = item.id)
        #TODO
        #A optimiser
        for jack in jacks :
            user[jack.id] = jack.id
    for carac in caracs :
        jacks = UserProfile.objects.filter(Caracs__id__icontains = carac.id)
        #TODO
        #A optimiser
        for jack in jacks :
            user[jack.id] = jack.id
    
    for id in user.keys() :
        #TODO
        #a verifier fait a l'arrache
        u = User.objects.get(id=id)
        try :
            notification = Notification.objects.get(ThreadEngine__id_icontains = threadEngine.id)
        except :
            notification =  Notification.objects.create()
        notification.ThreadEngine.add(threadEngine)
        notification.save()
        notificationuser = NotificationUser.objects.create(Notification=notification)
        notificationuser.save()
        u.get_profile().Notifications.add(notificationuser)
        u.get_profile().save()
        u.save()
        