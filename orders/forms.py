from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _
# create form from OrderCreateForm
class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':_('نام کوچک')}))
    last_name = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':_('نام خانوادگی')}))
    email = forms.EmailField(required=True, label=False ,widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    address = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':_('آدرس ')}))
    postal_code = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':_('کدپستی')}))
    city = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':_('شهر')}))

    
    class Meta:
        # The model of this form is Order
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
