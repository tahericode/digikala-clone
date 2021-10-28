from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import CouponApplyForm
from .models import Coupon

# def for Coupon
@require_POST   
def coupon_apply(request):
    now = timezone.now()
    # create a object from CouponApplyForm
    form = CouponApplyForm(request.POST)
    # form validation
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            #Get the object of Coupon model that matches the code entered and validation
            coupon = Coupon.objects.get(code__iexact = code,
                                        valid_from__lte = now,
                                        valid_to__gte = now,
                                        active = True) 
            # Put the code ID in the session
            request.session['coupon_id'] = coupon.id
        # if Coupon doas not exist 
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
            