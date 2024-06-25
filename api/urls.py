from django.urls import path, include
from api.views import PostView, PersonView

urlpatterns = [
    path('post/', PostView.as_view()),
    path('person/', PersonView.as_view()),
]