from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm

@require_POST
def cart_add(request, product_id):
    # create object from the Cart class
    cart = Cart(request)
    # get desired product  with id
    product = get_object_or_404(Product, id=product_id)
    # create a object from CartAddProductForm class
    form = CartAddProductForm(request.POST)
    # validation
    if form.is_valid():
    # cleaned data this from after validate
        cd = form.cleaned_data
    # add a cart for desired product
        cart.add(product=product, quantity=cd['quantity'], update_quantity = cd['update'])
    return redirect('cart:cart_detail')

# Remove products from the card
def cart_remove(request, product_id):
    # create object from the Cart class
    cart = Cart(request)
    # get desired product  with id
    product = get_object_or_404(Product, id=product_id)
    # remove the desired cart 
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    # create object from the Cart class
    cart = Cart(request)
    # loop for cart items
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                                        'quantity': item['quantity'],
                                                       'override': True})
    # create object from CouponApplyForm class
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/detail.html', {'cart':cart, 'coupon_apply_form': coupon_apply_form})
    



