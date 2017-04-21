from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from VoxPomona.models import UserInfo


class SignUpForm(forms.ModelForm):
    email = forms.CharField(label='email', max_length=500)
    full_name = forms.CharField(label='name', max_length=128)

    password = forms.CharField(label='password', max_length=128, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) > 29:
            raise forms.ValidationError("Sorry, this email is too large.")
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('Email addresses must be unique.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) <= 6:
            raise forms.ValidationError('Password must be longer than 6 characters.')
        return password

    class Meta:
        model = UserInfo
        fields = ('email', 'name', 'user_type')

