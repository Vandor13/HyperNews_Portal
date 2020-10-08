from django.urls import path, re_path
from . import views
from .views import NewsView

urlpatterns = [path("", views.home, name="home"),
               re_path("news/(?P<news_id>[^/]*)/?", NewsView.as_view()),
               ]
