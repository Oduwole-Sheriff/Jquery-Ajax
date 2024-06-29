from django.urls import path, include
from api.views import PostView, PersonView, LanguageView

urlpatterns = [
    path('post/', PostView.as_view()),
    path('person/', PersonView.as_view()),
    path('language/', LanguageView.as_view()),
]