from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.PostListView, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('order/<int:pk>/', PostDetailView.as_view(), name='order-detail'),
    path('order/new/', PostCreateView.as_view(), name='new-order'),
    path('order/<int:pk>/update/', PostUpdateView.as_view(), name='update-order'),
    path('order/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-order'),
]