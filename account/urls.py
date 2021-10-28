from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import forms 


urlpatterns = [
    # dashboard 
    path('', views.displayUserInformation, name='dashboard'),
    # login user
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.CustomAuthForm), name='login'),
    # logout user
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change user password
    path('password_change/', auth_views.PasswordChangeView.as_view(form_class=forms.CustomPassChangeForm), name='password_change'),
    # Go to this address when the password change is successful
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset user password
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=forms.CustomEmailForm), name='password_reset'),
    # Go to this address when the password reset is successful
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # password reset confirm
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=forms.CustomResetPassForm), name='password_reset_confirm'),
    # when password reset complete
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # user register
    path('register/', views.register, name='register'),
    # edit user profile
    path('edit/', views.edit, name='edit'),
    # add to favorite list
    path('fav/<int:id>', views.favorite_add, name='favorite_add'),
    # favorite list
    path('favorite/', views.favorite_list, name='favorite_list'),
    # displayUserInformation
    path('displayUserInformation/', views.displayUserInformation, name='displayUserInformation'),
    # userComments
    path('usercomments/', views.userComments, name='userComments')
]
