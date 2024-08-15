from django.shortcuts import render, redirect
from my_app.forms import registrations
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from posts.models import Post
from author.models import author
# Create your views here.

def home(request):
    data = Post.objects.all()
    posts_count = data.count()  
    return render(request,'index.html', {'data': data , 'posts_count': posts_count})

def register(request):
    if request.method == 'POST':
        form = registrations(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    else:
        form = registrations()    
    return render(request,'register.html' ,{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request , data = request.POST )
        if form.is_valid():
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            user =authenticate( username = u_name, password = u_pass )
            if user is not None:
                login(request, user )  
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render( request, 'login.html', {'form': form })        

def user_logout(request): 
    logout(request)
    return redirect('login')

    