from django.db import models
from django.db.models import fields
from django.forms import forms
from .models import Comment
from django import forms
        

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    body = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':'پیام شما'}))
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
