from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from . models import Profile
import datetime

#Login Form
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=TextInput(attrs={'class':'validate','placeholder': 'نام کاربری یا ایمیل خود را وارد کنید...'}))
    password = forms.CharField(label=False, widget=PasswordInput(attrs={'placeholder': 'رمز عبور'}))


#Email Form
class CustomEmailForm(PasswordResetForm):
    email = forms.EmailField(label=False, max_length=254, widget=TextInput(attrs={'class':'validate','placeholder': 'ایمیل'}))

#Change pass Form
class CustomPassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'autofocus': True, 'placeholder': "رمز عبور قدیمی"}))
    new_password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder': "رمز عبور جدید"}))
    new_password2 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder':"تایید رمز عبور جدید"}))

#Resetpasspassword
class CustomResetPassForm(SetPasswordForm):
     new_password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder': "رمز عبور جدید"}))
     new_password2 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder':"تایید رمز عبور جدید"}))

#Registeration
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':"تایید رمز عبور"}))

    class Meta:
        model = User
        fields = ('username', 'email')
    
    
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('قبلا با ایمیل ثبت نام انجام شده است')
        return cd['email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError('عدم تطابق رمز های عبوریکبار دیگر تلاش کنید!!!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'نام کوچک'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':' نام خانوادگی'}))
    email = forms.EmailField(label=False ,widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='تاریخ تولد',initial=datetime.date, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    photo = forms.ImageField(label=False, allow_empty_file=True, required=False)
    address = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'آدرس '}))
    postal_code = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={'placeholder':'کدپستی'}))
    city = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'شهر'}))
    class Meta:
        model = Profile
        fields = ('date_of_birth','address','postal_code' ,'city', 'photo')