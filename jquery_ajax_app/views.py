from django.shortcuts import render, redirect
from jquery_ajax_app.forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'jquery_ajax_app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context
    

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
