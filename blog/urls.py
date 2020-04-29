from django.urls import path, include
from . import views
from .models import Post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('/<int:pk>', views.post_detail, name='post_detail'),
    path('/new/', views.post_new, name='post_new'),
]
