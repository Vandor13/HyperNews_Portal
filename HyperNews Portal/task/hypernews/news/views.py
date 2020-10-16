from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.conf import settings
import json
from itertools import groupby
import datetime

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


class AllNewsView(View):
    def get(self, request, *args, **kwargs):
        file_name = settings.NEWS_JSON_PATH

        with open(file_name) as file:
            news = json.load(file)
        news.sort( key=get_date, reverse = True)
        for article in news:
            article["href"] = get_link(article)
        iterator = groupby(news, key=get_date)
        news_by_date = []
        for date, x in iterator:
            news_by_date.append({"date": str(date), "news": list(x)})
        context = {"news": news_by_date}
        return render(
            request, 'news/all_news.html', context=context
        )


class CreateNewsView(View):
    def post(self):
        pass


def home(request):
    return HttpResponse("Coming soon")


def get_date(article):
    datetime_object = datetime.datetime.strptime(article["created"], "%Y-%m-%d %H:%M:%S")
    return datetime_object.date()


def get_link(article):
    return "/news/" + str(article["link"]) + "/"


# with open("news.json") as file:
#     news = json.load(file)
# # print(news)
# news.sort(key=get_date)
# # print(news)
# iterator = groupby(news, key=get_date)
# news_by_date = []
# for date, x in iterator:
#     news_by_date.append([str(date), list(x)])
# # print(news_by_date)
