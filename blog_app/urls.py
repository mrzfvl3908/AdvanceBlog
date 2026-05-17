from django.urls import path
from . import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostListView.as_view(), name='post_list'),
]