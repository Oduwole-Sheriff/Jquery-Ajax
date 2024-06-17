from django.urls import path, include
from api.views import PostView

urlpatterns = [
    path('post/', PostView.as_view()),
]