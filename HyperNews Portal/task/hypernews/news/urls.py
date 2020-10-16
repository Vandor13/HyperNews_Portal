from django.urls import path, re_path
from . import views
from .views import NewsView, AllNewsView, CreateNewsView

urlpatterns = [path("", views.home, name="home"),
               path("news/", AllNewsView.as_view()),
               path("news/create/", CreateNewsView.as_view()),
               re_path("news/(?P<news_id>[^/]*)/?", NewsView.as_view()),
               ]
