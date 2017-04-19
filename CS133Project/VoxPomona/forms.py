from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required field.')
    first_name = forms.CharField(max_length=30, help_text='Required field.')
    last_name = forms.CharField(max_length=30, help_text='Required field.')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')