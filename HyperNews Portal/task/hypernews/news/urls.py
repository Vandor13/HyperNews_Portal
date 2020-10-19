from django.urls import path, re_path
from . import views
from .views import NewsView, AllNewsView, CreateNewsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("", views.home, name="home"),
               path("news/", AllNewsView.as_view()),
               path("news/create/", CreateNewsView.as_view()),
               re_path("news/(?P<news_id>[^/]*)/?", NewsView.as_view()),
               ]

urlpatterns += static(settings.STATIC_URL)