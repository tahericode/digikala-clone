from shop.models import Product
from django.shortcuts import render, redirect
from . import models
from cart.cart import Cart
from .forms import OrderCreateForm
from django.urls import reverse



def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
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
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

            