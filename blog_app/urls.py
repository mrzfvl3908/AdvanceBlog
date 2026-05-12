from django.urls import path
from . import views

urlpatterns = [
    path('posts_list', views.IndexView.as_view(), name='index'),
]