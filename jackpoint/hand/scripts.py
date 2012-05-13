from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from skill.models import Skill
from carac.models import Carac
from item.models import Item
from carac.forms import CaracFormChoice
from skill.forms import SkillForm
from item.forms import ItemForm
from jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from hand.forms import AskForm
from hand.models import Question,Answer
from jack.models import CaracUser,SkillUser,ItemUser
from tag.models import Tag
from engine.models import ThreadEngine
from engine.script import sendnotification
#TODO
# A factyoriser enregistrement skills carac items



def enregistrementAnswer(request):
        user = User.objects.get(id=request.user.id)
        reponse  = request.POST['Reponse']
        tags  = request.POST['Tags']
        threadengineid  = int(request.POST['ThreadEngineId'])
        threadengine = ThreadEngine.objects.get(id=threadengineid)
        questionid = int(request.POST['QuestionId'])
        tags = tags.split("#")
        question = Question.objects.get(id=questionid)
        answer = Answer.objects.create(user=user,Text=reponse)
        answer.Question.add(question)
        #TODO
        # a factoriser
        for tag in tags :
            tag = tag.strip()
            try :
                result = Tag.objects.get(Name=tag)
            except :
                result = Tag.objects.create(Name=tag)
            result.save()
        answer.Tags.add(result)
        answer.save()
        threadengine.Answer.add(answer)
        threadengine.save()

def enregistrementAsk(request,caracs,skills,items,intitule,description,tags) :
    question = Question.objects.create() 
    question.save()
    question.user =  User.objects.get(id=request.user.id)
    question.Text = description
    question.Intitule = intitule
    question.save()
    #TODO
    #Factoriser et expliquer les tags
    tags = tags.split('#')
    # TODO
    # A factoriser
    for tag in tags :
        tag = tag.strip()
        try :
            result = Tag.objects.get(Name=tag)
        except :
            result = Tag.objects.create(Name=tag)
            result.save()
        question.Tags.add(result)
    question.save()
    for carac in caracs.keys():
        caracdb  = Carac.objects.get(Nom=carac)
        try :
            result = CaracUser.objects.get(carac=caracdb,Level=int(caracs[carac][0]))
        except :
            result = CaracUser.objects.create(Level=0)
            result.Carac.add(caracdb)
            result.Level = int(caracs[carac][0])
            result.save()
        question.Caracs.add(result)
    for skill in skills.keys():
        skilldb  = Skill.objects.get(Nom=skill)
        print "nomSki"
        print skilldb.Nom
        private = False
        try :
            result = SkillUser.objects.get(Skills=skilldb,Level=int(skills[skill][0]))
        except :
            result = SkillUser.objects.create(Level=0)
            result.Skill.add(skilldb)
            result.Private = private
            result.Level = int(skills[skill][0])
            result.save()
        question.Skills.add(result)
    for item in items.keys():
        itemdb  = Item.objects.get(Nom=item)
        try :
            result = ItemUser.objects.get(Item=itemdb)
        except :
            result = ItemUser.objects.create()
            result.Item.add(itemdb)
            result.Private = private
            result.save()
        question.Items.add(result)
    question.save()
    threadengine = ThreadEngine.objects.create()
    threadengine.Question.add(question)
    threadengine.save()
    sendnotification(question,threadengine)

    