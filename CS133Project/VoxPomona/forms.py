from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from VoxPomona.models import UserInfo


class SignUpForm(forms.ModelForm):
    email = forms.CharField(label='email', max_length=500)
    password = forms.CharField(label='password', max_length=128, widget=forms.PasswordInput)

    #Ensure appropriate email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) > 29:
            raise forms.ValidationError("Sorry, this email is too large.")
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('There is already an account associated with this email.')
        return email

    #Ensure password length
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) <= 6:
            raise forms.ValidationError('Password must be longer than 6 characters.')
        return password

    class Meta:
        model = UserInfo
        fields = ('email', 'name', 'user_type')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder' : 'Email'})
        self.fields['email'].label = ''

        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder' : 'Full name'})
        self.fields['name'].label = ''

        self.fields['user_type'].widget.attrs.update({'class' : 'form-control'})
        self.fields['user_type'].label = 'User type'
        self.fields['user_type'].help_text = 'Click to select your user type'

        self.fields['password'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder' : 'Password'})
        self.fields['password'].label = ''

