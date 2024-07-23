from django.contrib.auth.decorators import login_required
from django.shortcuts import render,   get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blogs
from . forms import BlogsForm
from django.urls import reverse_lazy


# Create your views here.

# def home(request):
#   return render(request, 'home.html', {})


class HomeView(ListView):
    model = Blogs
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Blogs
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Blogs
    template_name = 'add_post.html'

    form_class = BlogsForm

class UpdatePostView(UpdateView):
    model = Blogs
    template_name = 'update_post.html'
    fields = ['title', 'content']


class DeletePostView(DeleteView):
    model = Blogs
    template_name = 'delete_post.html'
    success_url =  reverse_lazy('home')