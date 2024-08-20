from django.shortcuts import render, redirect
from my_app.forms import registrations, updateuser
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from posts.models import Post
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

    
 
def updateProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = updateuser(request.POST,instance = request.user)
            if form.is_valid():
                form.save()
                return redirect ('login')
        else:
            form = updateuser(instance = request.user)    
        return render(request,'changeuser.html' ,{'form':form}) 
    else:
        return redirect('login')   
    

def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect ('homepage')
        else:
            form = PasswordChangeForm(user = request.user)    
        return render(request,'changepass.html' ,{'form':form}) 
    else:
        return redirect('login') 
