from django.urls import path, re_path
from . import views
from .views import NewsView

urlpatterns = [path("", NewsView.as_view()),
               re_path("news/(?P<news_id>[^/]*)/?", NewsView.as_view()),
               ]
