from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class NewsView(View):
    def get(self, request, news_id=0, *args, **kwargs):
        return render(
            request, 'news/news.html'
        )

def home(request):
    def get(self, get_request, *args, **kwargs):
        # context = {"news_id": news_id}
        return "Coming soon"
