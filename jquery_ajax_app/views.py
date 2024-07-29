from django.shortcuts import render, redirect
from jquery_ajax_app.forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'jquery_ajax_app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context
        
    def test_func(self):
        # Example: Allow access only to logged-in users
        return self.request.user.is_authenticated


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'drink', 'image']

    def get_success_url(self):
        return reverse_lazy('home') 


class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'drink', 'image']
