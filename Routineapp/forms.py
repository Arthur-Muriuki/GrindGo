from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Routine

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['title', 'day', 'time', 'description']
