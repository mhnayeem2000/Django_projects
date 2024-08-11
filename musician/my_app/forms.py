from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from my_app.models import musicians, album 

class registrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'id': 'required'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1','password2' ]
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }



class update_user(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'id': 'required'}))
    password = None
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


class add_musicians(forms.ModelForm):
    class Meta:
        model = musicians
        fields = '__all__'
    

class add_album(forms.ModelForm):
    class Meta:
        model = album
        fields = '__all__'