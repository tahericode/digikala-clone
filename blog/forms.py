from django.db import models
from django.db.models import fields
from django.forms import forms
from django.forms.fields import EmailField
from django.forms.widgets import TextInput, Textarea
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    name = forms.CharField(label=False, max_length=50, widget=TextInput(attrs={'placeholder':'نام و نام خانوادگی'}))
    email = forms.EmailField(label=False, max_length=60, widget=TextInput(attrs={'placeholder':'ایمیل'}))
    body = forms.CharField(label=False, widget=Textarea(attrs={'placeholder':'نظرا خود را وارد کنید'}))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
            