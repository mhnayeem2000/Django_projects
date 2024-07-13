from django.shortcuts import render,redirect
from . import models
# Create your views here.

def home(request):
    student = models.User.objects.all()
    return render(request, 'home.html', {'student': student})


def delete(request,uid):
    dlt = models.User.objects.get( pk = uid).delete()
    return redirect("homepage")

