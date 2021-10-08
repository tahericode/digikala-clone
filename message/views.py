from django import contrib
from django.shortcuts import get_object_or_404, render
from .import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def publicMessages(request):
    messages = models.PublicMassages.objects.filter(status='published').order_by('-created')
    context = {
        'messages':messages
    }
    return render(request, 'message/publicMessage.html', context)

@login_required
def detailPublicMessage(request, id):
    message = get_object_or_404(models.PublicMassages, id=id)
    context = {
        'message':message
    }
    return render(request, 'message/detailPublicMessage.html', context)

@login_required
def privateMessages(request):
    user = get_object_or_404(User, username = request.user.username)
    messages = models.PrivateMassages.objects.filter(status = 'published').filter(user=user)
    
    context = {
        'user':user,
        'messages':messages
    }
    return render(request, 'message/privateMessage.html', context)

@login_required
def detailPrivateMessage(request, id):
    message = get_object_or_404(models.PrivateMassages, id = id)
    context = {
        'message':message
    }
    return render(request, 'message/detailPrivateMessage.html', context)
