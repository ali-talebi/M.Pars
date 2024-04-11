from django import forms
from .models import Comments_Weblog

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments_Weblog
        fields = ['title', 'text']