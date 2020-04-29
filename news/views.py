from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from news.models import Articles

class Postlist(ListView):
    model = Articles
# Create your views here.
def news_list(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/posts.html', {'posts': news})

def news_detail(request, id):
    news = get_object_or_404(Articles, pk=id)
    return render(request, 'news/news_detail.html', {'news': news})
