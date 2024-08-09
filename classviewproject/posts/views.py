from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models
from posts.forms import post_form


class add_post(CreateView):
    model = models.posts
    form_class = post_form	
    template_name = 'posts.html'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        