from django.shortcuts import render,redirect
from . import models
from .forms import addstd
# Create your views here.

def home(request):
    student = models.User.objects.all()
    return render(request, 'home.html', {'student': student})


def delete(request,uid):
    dlt = models.User.objects.get( pk = uid).delete()
    return redirect("homepage")

def adduser_view(request):
    if request.method == 'POST':
        form = addstd(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    else:    
        form =  addstd()
    return render(request, 'home.html', {'form': form})


