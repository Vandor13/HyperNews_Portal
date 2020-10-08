from django.urls import path
from django.views import View


class CatView(View):
    pass


class DogView(View):
    pass


urlpatterns = [
    path("dog/", DogView.as_view()),
    path("cat/", CatView.as_view()),
]