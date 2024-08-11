from django.shortcuts import render, redirect
from author.forms import add_author
# Create your views here.

def add_authorr(request):
    if request.method == 'POST':
        form = add_author(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = add_author()    
    return render(request, 'author.html', {'form': form})