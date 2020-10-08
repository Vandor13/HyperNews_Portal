from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.conf import settings
import json
import os

# Create your views here.


class NewsView(View):
    def get(self, request, news_id=13, *args, **kwargs):
        # print("Hello")
        # file_name = str(os.path.dirname(os.path.abspath(__file__)))+ "\\" + settings.NEWS_JSON_PATH
        file_name = settings.NEWS_JSON_PATH
        # print(file_name)
        print(news_id)
        news_article = None
        if news_id:
            with open(file_name) as file:
                news = json.load(file)
                # print("Length of read json: " + str(len(news)))
                news_article = None
                news_article = [article for article in news if int(article["link"]) == int(news_id)]
            # print("News id is: " + str(news_id))
        # print("Length of news article: " + str(len(news_article)))
        if news_article and len(news_article) > 0:
            context = {"news": news_article[0]}
        else:
            context = {"news": "No news yet", "text": "No news article found"}
        return render(
            request, 'news/news.html', context=context
        )


def home(request):
    return HttpResponse("Coming soon")
