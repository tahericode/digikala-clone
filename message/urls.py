from django.urls import path
from .import views
app_name = 'message'

urlpatterns = [
    path('publicmessages', views.publicMessages, name='publicMessages'),
    path('publicMessages/<id>', views.detailPublicMessage, name='detailPublicMessages'),
    path("privateMessage", views.privateMessages, name="privateMessages"),
    path('privateMessage/<id>', views.detailPrivateMessage, name='detailPrivateMessages')
]
