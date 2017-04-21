from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from VoxPomona.models import UserInfo


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required field.')
    full_name = forms.CharField(max_length=30, help_text='Required field.')

    class Meta:
        model = UserInfo
        fields = ('email', 'name', 'user_type')