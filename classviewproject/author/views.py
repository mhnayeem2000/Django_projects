from django.shortcuts import render, redirect
from author.forms import registration_form
# Create your views here.

def add_authorr(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = registration_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_author')
        else:
            form = registration_form()    
        return render(request, 'author.html', {'form': form})
    else :
        return redirect('login')