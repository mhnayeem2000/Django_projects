from django.shortcuts import render,redirect
from . forms import registrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'home.html')

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

def user_create_success(request):
    return render(request, 'user_succ.html')