from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from blog_app.forms import PostForm
from blog_app.models import Post



class PostListView(ListView):
    # model = Post
    queryset = Post.objects.filter(status=True).order_by('-created_date')
    context_object_name = 'posts'
    paginate_by = 2

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['author','title', 'content', 'status', 'category','published_date']
    success_url = '/blog/post/'
