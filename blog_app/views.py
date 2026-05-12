from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog_app.models import Post


class IndexView(TemplateView):
    template_name = 'blog_app/posts_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
