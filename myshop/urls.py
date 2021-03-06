"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from details.views import change_lang
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    # third party(rosetta)
    path(_('rosetta/'), include('rosetta.urls')),
    # apps
    path(_('products/'),include('shop.urls', namespace='shop')),
    path(_(''),include('details.urls', namespace='details')),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('blog/'), include('blog.urls', namespace='blog')),
    path(_('account/'), include('account.urls')),
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    #CkEditor url for upload 
    path(_('ckeditor/'), include('ckeditor_uploader.urls')),
    path(_('messages/'), include('message.urls', namespace='message')),
    path('change_lang', change_lang, name='change_lang')
    
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

