from django import forms
from categories.models import category
from author.models import author
from posts.models import Post

class post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
