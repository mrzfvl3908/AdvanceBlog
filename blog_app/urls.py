from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]