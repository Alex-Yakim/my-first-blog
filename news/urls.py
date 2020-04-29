from django.urls import path, include
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.models import Articles
from news.views import Postlist
from . import views

urlpatterns = [
    #path('', Postlist.as_view(), template_name='news/posts.html'),
    #path('', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20], template_name='news/posts.html')),
    path('', views.news_list, name='news_list'),
    path('/<id>', views.news_detail, name='news_detail')
]
