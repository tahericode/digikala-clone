from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    # for product list
    path('', views.product_list, name='product_list'),
    # for product list by category
    path('<category_slug>', views.product_list, name= 'product_list_by_category'),
    # for detail product
    path('<int:id>/<slug>', views.product_detail, name='product_detail'),
    # for product list by tag
    path('tag/<slug:tag_slug>/',
        views.product_list, name='product_list_by_tag'),      
]
