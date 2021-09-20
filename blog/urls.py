from django.urls import path , re_path
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.post_list, name='post_list'),
  re_path(r'^(?P<category_slug>[-\w]+)/$', views.post_list, name='post_list_by_category'),
  re_path(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'), 
]