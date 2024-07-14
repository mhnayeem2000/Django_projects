from django import forms
from mydb.models import addusermodel

class addstd(forms.ModelForm):
    class Meta:
        model = addusermodel
        fields = '__all__'

        
