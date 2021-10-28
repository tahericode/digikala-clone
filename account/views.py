from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from shop.models import Product
from .forms import UserRegistrationForm, CustomAuthForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from .models import Profile 

# dashboard
@login_required
def dashboard(request):
    return render(request,
                'account/dashboard.html',
                {'section':'dashboard'})

# register
def register(request):
    if request.method == 'POST':
        #create an object from UserRegistrationForm
        user_form = UserRegistrationForm(request.POST)
        # Validation
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen  password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the User object
            new_user.save()
            #Create the user profile
            Profile.objects.create(user=new_user)
            # return redirect("userprofile:edit")
            return render(request, 'registration/register_done.html', {'new_user': new_user})    
    else:
        #If the request was not by post create an empty object from UserRegistrationForm
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


# edit user information
@login_required
def edit(request):
    # user = get_object_or_404(User, username=request.user.username)
    if request.method == 'POST':
        #Update user & profile object 
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        # Validation
        if user_form.is_valid() and profile_form.is_valid():
            # Save if the form is valid
            user_form.save()
            profile_form.save()
    else:
        #If the request was not by post create an object from UserEditForm & ProfileEditForm
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

# For displayUserInformation
@login_required
def displayUserInformation(request):
    return render(request, 'account/displayUserInformation.html', {})

# For user comments
@login_required
def userComments(request):
    return render(request, 'account/userComments.html', {})


# favorite list
@login_required
def favorite_list(request):
    # create an object from Product class
    new = Product.objects.filter(favorite = request.user)
    # return render
    return render(request, 'account/favorites.html', {'new':new})

# for add to fav list
@login_required
def favorite_add(request, id):
    # create an object from Product 
    product = get_object_or_404(Product, id=id)
    # for Remove from Favorites list
    if product.favorite.filter(id = request.user.id).exists():
        #Remove from Favorites list 
         product.favorite.remove(request.user)
    else:
        # for add to Favorites list
        product.favorite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    

    
    