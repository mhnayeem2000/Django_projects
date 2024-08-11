from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models
from posts.forms import post_form

def add_post(request):
    if request.method == 'POST':
        form = post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else:
        form = post_form()    
    return render(request, 'posts.html', {'form': form})


        