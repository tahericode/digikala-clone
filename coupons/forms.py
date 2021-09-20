from django import forms
from django.forms.widgets import TextInput

class CouponApplyForm(forms.Form):
    code = forms.CharField(label=False, widget=TextInput(attrs={'class':'form-control','placeholder': 'کد تخفیف خود را وارد کنید ...'}))