from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skill.models import Skill
from engine.models import ThreadEngine
from carac.models import Carac
from item.models import Item
from carac.forms import CaracFormChoice
from skill.forms import SkillFormChoice
from item.forms import ItemFormChoice
from django.forms.formsets import formset_factory
from hand.scripts import enregistrementAsk,enregistrementAnswer
from hand.forms import AskForm,AnswerForm



@login_required
def viewid(request,id):
    try :
        threadengine = ThreadEngine.objects.get(id=id)
    except :
        #Todo
        #renvoyer une 404
        threadengine = None
    if request.method == 'POST':
        enregistrementAnswer(request)
    qs= threadengine.Question.all()
    for q in qs :
        print q
        print q.id
        id = q.id
    form = AnswerForm(initial={'ThreadEngineId': threadengine.id,'QuestionId':id})
    print form
    return render_to_response('handviewid.html', {'threadengine':threadengine,'form':form
    },RequestContext(request))# Create



@login_required
def vieweditid(request,id):
    try :
        threadengine = ThreadEngine.objects.get(id=id)
    except :
        #Todo
        #renvoyer une 404
        threadengine = None
        pass
    form = AnswerForm()
    form.ThreadEngineId = threadengine.id
    print form
    print "titi"
    form.save()
    return render_to_response('handviewid.html', {'threadengine':threadengine,'form':form
    },RequestContext(request))# Create


@login_required
def index(request):
    threadengine = ThreadEngine.objects.all()
    return render_to_response('handview.html', {'threadengine':threadengine
    },RequestContext(request))# Create


@login_required
def ask(request):
    if request.method == 'POST': # If the form has been submitted...
        nbre_carac = int(request.POST['carac-TOTAL_FORMS'])
        nbre_initial_carac = request.POST['carac-INITIAL_FORMS']
        levelcarac="carac-#-carac_level"
        namecarac = "carac-#-carac"
        privatecarac = "carac-#-carac_private"
        compteur_carac = 0
        caracs = {}
        while compteur_carac < nbre_carac :
            if int(request.POST["carac-%d-carac_level"%compteur_carac]) >= 0 :
                caracs[request.POST["carac-%d-carac"%compteur_carac]] = [request.POST["carac-%d-carac_level"%compteur_carac]]
                compteur_carac += 1
        nbr_skills = int(request.POST['skill-TOTAL_FORMS'])
        nbr_initial_skills = request.POST['skill-INITIAL_FORMS']
        levelskill = "skill-#-skill_level"
        nameskill = "skill-#-skill"
        privateskill = "skill-#-skill_private"
        compteur_skill = 0
        skills = {}
        
        while compteur_skill < nbr_skills :
            if int(request.POST["skill-%d-skill_level"%compteur_skill]) >= 0 :
                skills[request.POST["skill-%d-skill"%compteur_skill]] = [request.POST["skill-%d-skill_level"%compteur_skill]]
            compteur_skill += 1
            
        nbre_item = int(request.POST['item-TOTAL_FORMS'])
        nbre_initial_item = request.POST['item-INITIAL_FORMS']
        Possede = "item-#-item_Possede"
        nameitem = "item-#-item"
        privatecarac = "item-#-item_private"
        compteur_item = 0
        items = {}
        while compteur_item < nbre_item :
            if int(request.POST["item-%d-item_Possede"%compteur_item]) > 0 :
                items[request.POST['item-%d-item'%compteur_item]] = request.POST["item-%d-item_private"%compteur_item]
            compteur_item += 1
        print caracs
        print skills
        print items
        description = request.POST['Description']
        intitule = request.POST['Intitule']
        tags = request.POST['Tags']
        retour = enregistrementAsk(request,caracs,skills,items,intitule,description,tags)  
        return HttpResponseRedirect('../../hand/view/') # Redirect after POST
    
    
    form = AskForm() # An unbound form
    Caracs = Carac.objects.all()
    Skills = Skill.objects.all()
    Items = Item.objects.all()
    initial = []
    for carac in Caracs :
        initial.append({'carac': carac.Nom,'id':carac.id})
    CaracFormSet = formset_factory(CaracFormChoice, extra=0)
    CaracFormSet = CaracFormSet(prefix='carac',initial=initial)
    initial = []
    # algo de skills a revoir pour le classement
    for skill in Skills :
        initial.append({'skill': skill.Nom,'id':skill.id})
    SkillFormSet = formset_factory(SkillFormChoice, extra=0)
    SkillFormSet = SkillFormSet(prefix='skill',initial=initial)
    initial = []
    for item in Items :
        initial.append({'item': item.Nom,'id':item.id})
    ItemFormSet = formset_factory(ItemFormChoice, extra=0)
    ItemFormSet = ItemFormSet(prefix='item',initial=initial)


    return render_to_response('ask.html', {
        'form': form,"CaracFormSet":CaracFormSet,'SkillFormSet':SkillFormSet,'ItemFormSet':ItemFormSet
    },RequestContext(request))# Create your views here.
    



