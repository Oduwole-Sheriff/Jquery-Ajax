from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

# def PostListView(request):
#     post = Post.objects.all()
#     context = {
#         'post': post,
#     }
#     return render(request, 'jquery_ajax_app/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'jquery_ajax_app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

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
