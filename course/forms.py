from django import forms
from .models import Course_Comments

class Course_CommentsForm(forms.ModelForm):

    class Meta:
        model = Course_Comments
        fields = ['title' , 'text' ]

