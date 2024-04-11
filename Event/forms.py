

from django import forms
from .models import Event_Comment
class EventForm(forms.ModelForm):

    class Meta:
        model = Event_Comment
        fields = ['title' , 'text']


