from jack.models import CaracUser,SkillUser,ItemUser,UserProfile
from hand.models import Question
from engine.models import Notification
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
        #TODO
        #Crade j'ai honte
        id = 0
        print "toto"
        print skill.Level
        print skill.Skill.all()
        for sk in skill.Skill.all() :
            print "toto"
            print sk
            id = sk.id
        print "sportid"
        print sk.id
        jacks = UserProfile.objects.filter(Q(Skills__Skill__id__contains = id),Q(Skills__Level__gte = skill.Level))
        
        print jacks
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
            notification = Notification.objects.get(ThreadEngine__id_icontains = threadEngine.id,User=u)
        except :
            notification =  Notification.objects.create(User=u)
            notification.ThreadEngine.add(threadEngine)
        notification.Url = "../../../hand/view/%d/"%threadEngine.id
        text = "Vous pouvez aider car vous avez : <br>"
        #TODO
        # Optimiser le double parcour
        
        for tag in tags :
            notification.Tags.add(tag)
        try:
            for skill in user[jack.id]['skill'] :
                notification.Skills.add(skill)
        except :
            pass
        try :      
            for item in user[jack.id]['item'] :
                notification.Items.add(item)
        except :
            pass
        try :
            for carac in user[jack.id]['carac'] :
                notification.Caracs.add(carac)
        except :
            pass
        notification.Texte = text    
        notification.save()
