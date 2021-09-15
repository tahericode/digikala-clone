from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'نام کوچک'}))
    last_name = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':' نام خانوادگی'}))
    email = forms.EmailField(required=True, label=False ,widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    address = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'آدرس '}))
    postal_code = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'کدپستی'}))
    city = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'شهر'}))

    
    class Meta:
        
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
