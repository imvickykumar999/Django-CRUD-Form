
from django import forms
from .models import GeeksModel

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = ['title', 'description', 'foto']
