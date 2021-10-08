from decimal import Context
from django import template
from weasyprint.css.computed_values import content
from shop.models import Product
from django.shortcuts import render, redirect,get_object_or_404
from .import models
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import OrderCreateForm
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import User


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(models.Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'orders/css/pdf.css')])
    return response


@login_required
def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(data=request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if not request.user.is_anonymous :
                order.user = request.user
            order.save()
            for item in cart:
                models.OrderItem.objects.create(order=order,
                                                product=item['product'],
                                                price = item['price'], 
                                                quantity=item['quantity'])
            # clear the cart
            cart.clear()
            
            # launch asynchronous task
            # order_create.delay(order.id)
            return render(request, 'orders/order/created.html', {'order':order})
    else:
        # add user if user loggin
        try:
            if request.user.profile:
                init={'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'city': request.user.profile.city,
                'postal_code': request.user.profile.postal_code,
                'address': request.user.profile.address, 
                }
                form = OrderCreateForm(initial=init)
        except:
            form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

            

@login_required
def order_pdf(request, order_id):
    order = get_object_or_404(models.Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    
    

    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'orders/css/pdf.css')])
    return response


@login_required
def orderTracking(request):
    orderTracking = models.Order.objects.filter(user = request.user)
    
    return render(request, 'orders/order/orderTracking.html', {'orderTracking':orderTracking})

def detailOrderTracking(request, order_id):
    order = get_object_or_404(models.Order, id = order_id)
    return render(request, 'orders/order/detailOrderTracking.html', {'order':order})



