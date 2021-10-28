from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from . models import Profile
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


from django.utils.translation import gettext_lazy as _

import datetime

#Login Form
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=TextInput(attrs={'class':'validate','placeholder': _('نام کاربری یا ایمیل خود را وارد کنید...')}))
    password = forms.CharField(label=False, widget=PasswordInput(attrs={'placeholder': _('رمز عبور خود را وارد کنید')}))

#Email Form
class CustomEmailForm(PasswordResetForm):
    email = forms.EmailField(label=False, max_length=254, widget=TextInput(attrs={'class':'validate','placeholder': _('ایمیل')}))

#Change pass Form
class CustomPassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_(''), strip=False, widget=forms.PasswordInput(attrs={'autofocus': True, 'placeholder': _("رمز عبور قدیمی")}))
    new_password1 = forms.CharField(label=_(''), strip=False, widget=forms.PasswordInput(attrs={'placeholder': _("رمز عبور جدید")}))
    new_password2 = forms.CharField(label=_(''), strip=False, widget=forms.PasswordInput(attrs={'placeholder':_("تایید رمز عبور جدید")}))

#Resetpasspassword
class CustomResetPassForm(SetPasswordForm):
     new_password1 = forms.CharField(label=_(''), strip=False, widget=forms.PasswordInput(attrs={'placeholder': _("رمز عبور جدید")}))
     new_password2 = forms.CharField(label=_(''), strip=False, widget=forms.PasswordInput(attrs={'placeholder':_("تایید رمز عبور جدید")}))

#Registeration 
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label=_('نام کاربری'), widget=forms.TextInput(attrs={'placeholder':_('نام کاربری')}))
    email = forms.EmailField(label=_(''), widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    password = forms.CharField(label=_(''), widget=forms.PasswordInput(attrs={'placeholder': _('رمز عبور')}))
    password2 = forms.CharField(label=_(''), widget=forms.PasswordInput(attrs={'placeholder':_("تایید رمز عبور")}))
    # The model of this form is user
    class Meta:
        # The model of this form is User
        model = User
        fields = ('username', 'email')
   # clean email for Email Form Validation
    def clean_email(self):
        cd = self.cleaned_data
        #If there is an email entered in the database
        if User.objects.filter(email=cd['email']).exists():
            # raise form validations error for email
            raise forms.ValidationError(_('قبلا با ایمیل ثبت نام انجام شده است'))
        return cd['email']
    # clean password2 for password Form Validation
    def clean_password2(self):
        cd = self.cleaned_data
        # if password not equal to the password2
        if cd['password'] != cd['password2'] :
            # raise form validations error for password
            raise forms.ValidationError(_('عدم تطابق رمز های عبوریکبار دیگر تلاش کنید!!!'))
        return cd['password2']

# for edit user information
class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label=_('نام'), widget=forms.TextInput(attrs={'placeholder':_('نام کوچک')}))
    last_name = forms.CharField(label=_('نام خانوادگی'), widget=forms.TextInput(attrs={'placeholder':_(' نام خانوادگی')}))
    email = forms.EmailField(label=_('ایمیل') ,widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    class Meta:
        # The model of this form is Userr
        model = User
        fields = ('first_name', 'last_name', 'email')

# for user profile information
class ProfileEditForm(forms.ModelForm):
    date_of_birth = JalaliDateField(label=_('تاریخ تولد'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
    photo = forms.ImageField(label=False, allow_empty_file=True, required=False)
    address = forms.CharField(required=True, label=_('آدرس'), widget=forms.TextInput(attrs={'placeholder':_('آدرس')}))
    postal_code = forms.CharField(required=False, label=_('کدپستی'), widget=forms.TextInput(attrs={'placeholder':_('کدپستی')}))
    city = forms.CharField(required=True, label=_('شهر'), widget=forms.TextInput(attrs={'placeholder':_('شهر')}))
    class Meta:
        # The model of this form is Profile
        model = Profile
        fields = ('date_of_birth','address','postal_code' ,'city', 'photo')