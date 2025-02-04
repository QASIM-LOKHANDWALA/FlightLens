from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']


def register_view(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dashboard')
  else:
    form = CustomUserCreationForm()
  
  return render(request, 'user_auth/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('dashboard')
  else:
    form = AuthenticationForm()
  
  return render(request, 'user_auth/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('login')

def dashboard_view(request):
  return render(request, 'user_auth/dashboard.html')