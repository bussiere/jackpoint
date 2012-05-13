# Create your views here.
from django.db import models
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response

from mp.scripts import SendMP
from mp.forms import  MPForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request,id):
    if request.method == 'POST':
        sender = User.objects.get(id=request.user.id)
        message = request.POST['Message']
        receiver = request.POST['Id_Destinataire']
        receiver = user = User.objects.get(id=int(receiver))
        SendMP(message,sender,receiver)
        return HttpResponseRedirect('../../X/')
    form =  MPForm(initial={'Id_Destinataire':id})
    return render_to_response('mp.html',{'form':form,'id':id},RequestContext(request))# Create