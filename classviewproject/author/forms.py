from django import forms
from author.models import author

class add_author(forms.ModelForm):
    class Meta:
        model = author
        fields = '__all__'


