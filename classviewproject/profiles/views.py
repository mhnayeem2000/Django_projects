from django.shortcuts import render, redirect

# Create your views here.
def profiles(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else: 
        return redirect('login')