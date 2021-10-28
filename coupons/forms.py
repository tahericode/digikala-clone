from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _
#create form for coupon code
class CouponApplyForm(forms.Form):
    code = forms.CharField(label=False, widget=TextInput(attrs={'class':'form-control','placeholder': _('کد تخفیف خود را وارد کنید ...')}))