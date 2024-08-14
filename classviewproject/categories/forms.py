from django import forms
from categories.models import category

class create_category(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'