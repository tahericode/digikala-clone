from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

#create form for QuestionForm
class QuestionForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':_('نام و نام خانوادگی')}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':_('موضوع')}))
    description = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':_('پیام شما')}))
    class Meta:
        # The model of this form is Question
        model = models.Question
        fields = ['name', 'email',  'subject', 'description']

# create form for Contact us     
class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':_('نام و نام خانوادگی')}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    tel = forms.CharField(label=False, max_length=13, widget=forms.TextInput(attrs={'placeholder':_('تلفن همراه')}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':_('موضوع')}))
    description = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':_('پیام شما')}))
    class Meta:
        # The model of this form is ContactUs
        model = models.ContactUs
        fields = ['name', 'email',  'subject', 'description']
    