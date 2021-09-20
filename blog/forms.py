from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _

#Create Comment Form
class CommentForm(forms.ModelForm):
    body = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':_('دیدگاه خود را ثبت کنید')}))
    class Meta:
        model = Comment
        fields = ('body',)