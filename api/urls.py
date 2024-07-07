from django.urls import path, include
from api.views import PostView, PersonView, LanguageView, LoginAPI, ResgisterAPI, ProfileView

urlpatterns = [
    path('post/', PostView.as_view()),
    path('person/', PersonView.as_view()),
    path('language/', LanguageView.as_view()),
    path('login/', LoginAPI.as_view()),
    path('register/', ResgisterAPI.as_view()),
    path('profile/', ProfileView.as_view()),
]