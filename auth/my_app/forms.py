from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

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


