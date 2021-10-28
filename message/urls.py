from django.urls import path
from .import views
# app name
app_name = 'message'

urlpatterns = [
    # for public messages
    path('publicmessages', views.publicMessages, name='publicMessages'),
    # for detail public messages
    path('publicMessages/<id>', views.detailPublicMessage, name='detailPublicMessages'),
    # for private messages
    path("privateMessage", views.privateMessages, name="privateMessages"),
    # for detail private messages
    path('privateMessage/<id>', views.detailPrivateMessage, name='detailPrivateMessages')
]
