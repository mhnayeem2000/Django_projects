from django.shortcuts import render
from .forms import contactForm

def contact(request):
    name = email =  None
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
    else:
        form = contactForm()

    return render(request, 'index.html', {"form": form , "name": name, "email": email})
