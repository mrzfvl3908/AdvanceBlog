from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from blog_app.models import Post


# class IndexView(TemplateView):
#     template_name = 'blog_app/post_list.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         return context


class PostListView(ListView):
    # model = Post
    queryset = Post.objects.filter(status=True).order_by('-created_date')
    context_object_name = 'posts'
    paginate_by = 1

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(DetailView):
    model = Post
