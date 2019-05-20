from django import forms
from .models import Tastyroad, Comment

class TastyroadForm(forms.ModelForm):
    class Meta:
        model= Tastyroad
        fields= {'title', 'text', }

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('nickname', 'text',)      