from django.shortcuts import render, redirect
from categories.forms  import create_category
# Create your views here.

def add_category(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            form = create_category(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_category')
        else:
            form = create_category()
        return render(request, 'category.html', {'form': form})
    else :
        return redirect('login')
