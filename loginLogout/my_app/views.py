from django.shortcuts import render , redirect
from my_app.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def home(request):
    return render(request, 'index.html')

def registration_views(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST ) 
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form }) 


def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            userPass = form.cleaned_data['password']
            user = authenticate(username = userName, password = userPass)
            if user is not None:
                login(request, user )
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form })

def userProfile(request):
    return render(request, 'profile.html', {'user': request.user})

def userLogout(request):
    logout(request)
    return redirect('login')

