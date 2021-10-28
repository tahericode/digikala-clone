from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    # cart detail
    path('', views.cart_detail, name='cart_detail'),
    # add product to cart
    path('add/<product_id>/', views.cart_add, name='cart_add'),
    # remove product from cart
    path('remove/<product_id>', views.cart_remove, name='cart_remove')
]
