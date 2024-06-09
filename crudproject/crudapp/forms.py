
from django import forms
from .models import GeeksModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = ['title', 'description', 'foto']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
