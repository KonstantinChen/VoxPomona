from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from VoxPomona.forms import *
from VoxPomona.models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. I'm hungry")

#User Registration
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # User default
            user = User.objects.create_user(form.cleaned_data.get('email'),
                form.cleaned_data.get('email'), form.cleaned_data.get('password'))
            name = form.cleaned_data.get('name')
            nameL = name.split()
            if (len(nameL) < 2):
                user.first_name = "failed"
                user.last_name = "name_creation"
            else:
                user.first_name = nameL[0]
                user.last_name = nameL[1]
            user.save()

            #Create UserInfo to retain other info
            user_info = UserInfo()
            user_info.email = form.cleaned_data.get('email')
            user_info.name = form.cleaned_data.get('name')
            user_info.user_type = form.cleaned_data.get('user_type')
            user_info.user = user
            user_info.save()

            return HttpResponse(user_info.user_type)

            # redirect to the profile page:
            user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return redirect('/VoxPomona/profile')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

#Logout Out: Simply logs out user and redirects to login
@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')

@login_required
def user_profile(request):
    return render(request, 'profile.html')