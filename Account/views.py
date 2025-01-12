from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from Hotelio.forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hotel_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_success(request):
    return render(request, 'logout_success.html')

def check_username(request, username):
    if User.objects.filter(username=username).exists():
        return HttpResponse("exists")
    return HttpResponse("available")

