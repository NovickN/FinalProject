from django import forms
from .models import Todo, Suggestions

class TodoForm(forms.ModelForm):
    class Meta: 
        model=Todo
        fields='__all__'

class SuggestionForm(forms.ModelForm):
    class Meta: 
        model=Suggestions
        fields='__all__'
