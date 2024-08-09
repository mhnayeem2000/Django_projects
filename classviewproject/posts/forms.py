from django import forms
from categories.models import category
from author.models import author
from posts.models import posts

class post_form(forms.ModelForm):
    class Meta:
        model = posts
        fields = '__all__'
