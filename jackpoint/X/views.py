# Create your views here.
from django.http import HttpResponseRedirect
from invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from invitation.models import Invitation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from engine.models import Notification
from mp.models import MP
from jack.models import UserProfile




@login_required
def index(request):
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(user=user)
    notifications = Notification.objects.filter(User=user)
    messagerecus = MP.objects.filter(Receiver=user)
    messageenvoyes = MP.objects.filter(Sender=user)
    return render_to_response('x.html', {'notifications':notifications,'messagerecus':messagerecus,'messageenvoyes':messageenvoyes,'profile':profile,'user':user
    },RequestContext(request))
