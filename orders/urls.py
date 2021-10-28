from os import name
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # for created
    path('created/',views.order_create, name='order_create' ),
    # admin pdf path 
    path('admin/order/<int:order_id>/pdf/',
        views.admin_order_pdf,
        name='admin_order_pdf'),
    # user pdf path
    path('order/<int:order_id>/pdf/',views.order_pdf,name='order_pdf'),
    # Order Tracking
    path('orderTracking', views.orderTracking, name="orderTracking"),
    # Detail orderTracking
    path('detail-orderTracking/<int:order_id>', views.detailOrderTracking, name="detailOrderTracking")
]
