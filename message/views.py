from django import contrib
from django.shortcuts import get_object_or_404, render
from .import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# def of PublicMessages
@login_required
def publicMessages(request):
    #get all objects of PublicMessages that filter by published
    
    return render(request, 'message/publicMessage.html', {})

# def of detailPublicMessage
@login_required
def detailPublicMessage(request, id):
    # Get an object from the public model that holds an input id
    message = get_object_or_404(models.PublicMassages, id=id)
    context = {'message':message}
    return render(request, 'message/detailPublicMessage.html', context)

# def of privateMessages
@login_required
def privateMessages(request):
    # get a desired user
    user = get_object_or_404(User, username = request.user.username)
    # get messages that match with desired user
    messages = models.PrivateMassages.objects.filter(status = 'published').filter(user=user)    
    context = {
        'user':user,
        'messages':messages}
    return render(request, 'message/privateMessage.html', context)

# def of detailPrivateMessage
@login_required
def detailPrivateMessage(request, id):
    # Get an object from the PrivateMassages model that holds an input id
    message = get_object_or_404(models.PrivateMassages, id = id)
    context = {'message':message}
    return render(request, 'message/detailPrivateMessage.html', context)
