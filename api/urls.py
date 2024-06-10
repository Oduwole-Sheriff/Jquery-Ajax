from django.urls import path, include
from jquery_ajax_app.views import PostView

urlpatterns = [
    path('post/', PostView.as_view()),
]