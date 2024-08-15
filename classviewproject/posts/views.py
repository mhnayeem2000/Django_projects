from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models
from posts.forms import post_form

def add_post(request):
    post = models.Post.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = post_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = post_form()    
        return render(request, 'posts.html', {'form': form})
    else:
        return redirect('login')
    
def edit_post(request , id):
    post = models.Post.objects.get(pk=id)
    form = post_form(instance=post)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = post_form(request.POST , instance= post)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = post_form(instance=post)    
        return render(request, 'posts.html', {'form': form})
    else:
        return redirect('login')    

def delete_post(request,id ):
    if request.user.is_authenticated:
        post = models.Post.objects.get(id=id)
        post.delete()
        return redirect('homepage')
    else: 
        return redirect('login')

        