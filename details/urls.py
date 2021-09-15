from django.urls import path
from . import views
app_name = 'details'

urlpatterns = [
    path('',views.home_pageView, name='homePage'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('about-us', views.about_us, name='about_us'),
    path('questions', views.questions, name='questions')
]