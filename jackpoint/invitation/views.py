from django.http import HttpResponseRedirect
from invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from invitation.models import Invitation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from skill.models import Skill
from carac.models import Carac
from item.models import Item
from carac.forms import CaracForm
from skill.forms import SkillForm
from item.forms import ItemForm
from jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from jack.scripts import enregistrementJack


def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FirstInvitationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            email = form.cleaned_data['Email']
            invitation = form.cleaned_data['Invitation']
            print email
            print invitation
            try :

                invitationdb = Invitation.objects.get(Code=invitation)
                user = User.objects.create_user(email, email, invitation)
                user.get_profile().InvitationAccepted = invitationdb
                user.get_profile().save()
                user.save()
                user = authenticate(username=email, password=invitation)
                auth.login(request, user)
                return HttpResponseRedirect('../invitation/inscription/')
            except Exception as inst:
                print type(inst)     # the exception instance
                print inst.args      # arguments stored in .args
                print inst 
                invitationdb = None
            if not invitationdb :
                return HttpResponseRedirect('../') # Redirect after POST
    else:
        form = FirstInvitationForm() # An unbound form

    return render_to_response('firstinvit.html', {
        'form': form,
    },RequestContext(request))# Create your views here.
    
@login_required
def invitation_inscription(request):
    #TODO
    # A REVOIR CRADE
    user = request.user
    if user.get_profile().Finished  == False :
        Caracs = Carac.objects.all()
        Skills = Skill.objects.all()
        Items = Item.objects.all()
        initial = []
        for carac in Caracs :
            initial.append({'carac': carac.Nom,'id':carac.id})
        CaracFormSet = formset_factory(CaracForm, extra=0)
        CaracFormSet = CaracFormSet(prefix='carac',initial=initial)
        initial = []
        # algo de skills a revoir pour le classement
        for skill in Skills :
            initial.append({'skill': skill.Nom,'id':skill.id})
        SkillFormSet = formset_factory(SkillForm, extra=0)
        SkillFormSet = SkillFormSet(prefix='skill',initial=initial)
        initial = []
        for item in Items :
            initial.append({'item': item.Nom,'id':item.id})
        ItemFormSet = formset_factory(ItemForm, extra=0)
        ItemFormSet = ItemFormSet(prefix='item',initial=initial)
        
        print CaracFormSet.management_form
        formJack = JackRegisterForm()
        return render_to_response('invitinscription.html',{"CaracFormSet":CaracFormSet,'SkillFormSet':SkillFormSet,'ItemFormSet':ItemFormSet,'formJack':formJack},RequestContext(request))
    else :
        return HttpResponseRedirect('../')
@login_required
def validation_inscription(request):
    #TODO
    # crade a revoir
    # passer par un base formset plutot qu'un truc crade comme ca.
    jack_username = request.POST['jack_username']
    jack_email = request.POST['jack_email']
    jack_password1 = request.POST['jack_password1']
    jack_password2 = request.POST['jack_password2']
    jack_Bio = request.POST['jack_Bio']
    jack = {}
    jack["jack_username"]=jack_username
    jack["jack_email"] = jack_email
    jack["jack_password1"]= jack_password1
    jack["jack_password2"]=jack_password2
    jack["jack_Bio"]=jack_Bio
    print jack["jack_username"]
    nbre_carac = int(request.POST['carac-TOTAL_FORMS'])
    nbre_initial_carac = request.POST['carac-INITIAL_FORMS']
    levelcarac="carac-#-carac_level"
    namecarac = "carac-#-carac"
    privatecarac = "carac-#-carac_private"
    compteur_carac = 0
    caracs = {}
    while compteur_carac < nbre_carac :
        caracs[request.POST["carac-%d-carac"%compteur_carac]] = [request.POST["carac-%d-carac_level"%compteur_carac],request.POST["carac-%d-carac_private"%compteur_carac]]
        compteur_carac += 1
        
    
    
    nbr_skills = int(request.POST['skill-TOTAL_FORMS'])
    nbr_initial_skills = request.POST['skill-INITIAL_FORMS']
    levelskill = "skill-#-skill_level"
    nameskill = "skill-#-skill"
    privateskill = "skill-#-skill_private"
    compteur_skill = 0
    skills = {}
    
    while compteur_skill < nbr_skills :
        if int(request.POST["skill-%d-skill_level"%compteur_skill]) > 0 :
            skills[request.POST["skill-%d-skill"%compteur_skill]] = [request.POST["skill-%d-skill_level"%compteur_skill],request.POST["skill-%d-skill_private"%compteur_skill]]
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
    print jack
    retour = enregistrementJack(request,jack,caracs,skills,items)  
    #TODO
    # a revoir ici 
    #Upload de file foireux
    jack_Avatar = request.FILES
    if retour :
        
        return HttpResponseRedirect('../../../X/')
    else :
        return HttpResponseRedirect('../../../invitation/')
        
        
    
@user_passes_test(lambda u: u.has_perm('invitation.Create_Invitation'), login_url='../../')
def create_invitation(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BaseFormSet(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            nombre = form.cleaned_data['NbreInvite']
            return HttpResponseRedirect('/admin/') # Redirect after POST
    else:
        form = CreateInvitationForm # An unbound form

    return render_to_response('createinvitation.html', {
        'form': form,
    })# Create your views here.

