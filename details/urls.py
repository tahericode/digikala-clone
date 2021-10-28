from django.urls import path
from . import views
# app_name
app_name = 'details'

urlpatterns = [
    # home page
    path('',views.home_pageView, name='homePage'),
    # contact us
    path('contact-us', views.contact_us, name='contact_us'),
    # about us
    path('about-us', views.about_us, name='about_us'),
    # questions
    path('questions', views.questions, name='questions')
]