# Third party imports.
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

# Local application imports.
from . import views

# Specifies the app's name.
app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name='home'),  # url for post list.
    path('user/<str:username>/',
         UserPostListView.as_view(),
         name='user-posts'),  # url for specific user post.
    path('post/<int:pk>/',
         PostDetailView.as_view(),
         name='post-detail'),  # url for post detail.
    path('post/new/',
         PostCreateView.as_view(),
         name='post-create'),  # url to create new post.
    path('post/<int:pk>/update/',
         PostUpdateView.as_view(),
         name='post-update'),  # url to update post.
    path('post/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),  # url to delete post.
    path('about/', views.about, name='about'),  # url for about page.
]

