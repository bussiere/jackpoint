from jackpoint.jack.models import CaracUser,SkillUser,ItemUser,UserProfile,NotificationUser
from jackpoint.hand.models import Question
from jackpoint.engine.models import Notification
from django.contrib.auth.models import User
from django.db.models import Q

#TODO
#A affiner si la personne peut repondre totalement a la question ou pas.
def sendnotification(question,threadEngine):
    skills = question.Skills.all()
    items = question.Items.all()
    caracs = question.Caracs.all()
    tags =  question.Tags.all()
    user = {}
    for skill in skills :
        jacks = UserProfile.objects.get(Q(Skills__id__icontains = skill.id),Q(Skills__Level__gte = skill.Level))
        #TODO
        #A optimiser
        for jack in jacks :
            try :
                user[jack.id]['skill'].append(skill)
            except :
                try :
                    user[jack.id]['skill'] = []
                    user[jack.id]['skill'].append(skill)
                except :
                    user[jack.id] = {}
                    user[jack.id]['skill'] = []
                    user[jack.id]['skill'].append(skill)
    for item in items :
        jacks = UserProfile.objects.filter(Items__id__icontains = item.id)
        #TODO
        #A optimiser
        for jack in jacks :
            try :
                user[jack.id]['item'].append(item)
            except :
                try :
                    user[jack.id]['item'] = []
                    user[jack.id]['item'].append(item)
                except :
                    user[jack.id] = {}
                    user[jack.id]['item'] = []
                    user[jack.id]['item'].append(item)
    for carac in caracs :
        jacks = UserProfile.objects.filter(Q(Caracs__id__icontains = carac.id),Q(Caracs__Level__gte = carac.Level))
        #TODO
        #A optimiser
        for jack in jacks :
            try :
                user[jack.id]['carac'].append(carac)
            except :
                try :
                    user[jack.id]['carac'] = []
                    user[jack.id]['carac'].append(carac)
                except :
                    user[jack.id] = {}
                    user[jack.id]['carac'] = []
                    user[jack.id]['carac'].append(carac)
                    
                    
                
    
    for id in user.keys() :
        #TODO
        #a verifier fait a l'arrache
        u = User.objects.get(id=id)
        try :
            notification = Notification.objects.get(ThreadEngine__id_icontains = threadEngine.id)
        except :
            notification =  Notification.objects.create()
            notification.ThreadEngine.add(threadEngine)
        notification.url = "../../../hand/view/%d/"%threadEngine.id
        text = "Vous pouvez aider car vous avez : <br>"
        #TODO
        # Optimiser le double parcour
        for tag in tags :
            notification.Tags.add(tag)
        for skill in user[jack.id]['skill'] :
              notification.Skill.add(skill)
        for item in user[jack.id]['item'] :
              notification.Item.add(item)
        for carac in user[jack.id]['carac'] :
            notification.Carac.add(carac)
        notification.Texte = text    
        notification.save()
        notificationuser = NotificationUser.objects.create(Notification=notification)
        notificationuser.save()
        u.get_profile().Notifications.add(notificationuser)
        u.get_profile().save()
        u.save()
        