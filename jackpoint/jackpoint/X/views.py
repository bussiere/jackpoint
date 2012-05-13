# Create your views here.
from django.http import HttpResponseRedirect
from jackpoint.invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from jackpoint.invitation.models import Invitation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from jackpoint.engine.models import Notification
from jackpoint.mp.models import MP





@login_required
def index(request):
    u = User.objects.get(id=request.user.id)
    
    notifications = Notification.objects.filter(User=u)
    messagerecus = MP.objects.filter(Receiver=u)
    messageenvoyes = MP.objects.filter(Sender=u)
    return render_to_response('x.html', {'notifications':notifications,'messagerecus':messagerecus,'messageenvoyes':messageenvoyes
    },RequestContext(request))
