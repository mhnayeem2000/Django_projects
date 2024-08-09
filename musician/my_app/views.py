from django.shortcuts import render,redirect
from .forms import registrationForm , update_user
from django.contrib.auth.forms import AuthenticationForm , SetPasswordForm , PasswordChangeForm 
from django.contrib.auth import  authenticate, login, logout , update_session_auth_hash
from . import models
# Create your views here.

def home(request):
    musician = models.musicians.objects.all()
    album = models.album.objects.all()
    return render(request, 'home.html',{'musicians':musician, 'album':album})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request= request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username = name, password = password)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()               
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')


def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = registrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = registrationForm()        
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('profile')
    

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =  PasswordChangeForm(user = request.user , data = request.POST)
            if form.is_valid():        
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'chagepass.html', {'form': form})
    else:
        return redirect('login')    

def change_password_without_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =  SetPasswordForm(user = request.user , data = request.POST)
            if form.is_valid():        
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'chagepass2.html', {'form': form})
    else:
        return redirect('login')    


def user_create_success(request):
    return render(request, 'user_succ.html')



def updateuser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = update_user(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = update_user(instance=request.user)        
        return render(request, 'update_user.html', {'form': form})
    else:
        return redirect('login')
    