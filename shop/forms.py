from django.forms import forms
from .models import Comment
from django import forms
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder':_('نام و نام خانوادگی')}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    body = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':_('پیام شما')}))
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']