from django.shortcuts import render
from myapp.forms import add_form

def home(request):
    return render(request, 'home.html')

def add_student(request):
    if request.method == 'POST':
        form = add_form(request.POST)
        if form.is_valid():
            form.save()
    else:        
        form = add_form()
    return render(request, 'home.html', {'form': form})





