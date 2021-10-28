from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-id')

class DetailNew(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'
