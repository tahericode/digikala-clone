
from django import forms
from . import models



class QuestionForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'موضوع'}))
    description = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':'پیام شما'}))
    class Meta:
        model = models.Question
        fields = ['name', 'email',  'subject', 'description']


    
class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    tel = forms.CharField(label=False, max_length=13, widget=forms.TextInput(attrs={'placeholder':'تلفن همراه'}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'موضوع'}))
    description = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':'پیام شما'}))
    class Meta:
        model = models.ContactUs
        fields = ['name', 'email',  'subject', 'description']
    