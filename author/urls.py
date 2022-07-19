from django.urls import path
from .views import AuthorDetailView, AuthorListView, AuthorPostsView, TopAuthorListView


urlpatterns = [
    path("author/", AuthorListView.as_view(), name='author'),
    path('author/<int:pk>/', AuthorDetailView.as_view()),
    path('author/<int:author_id>/posts/', AuthorPostsView.as_view()),
    path("author/top/", TopAuthorListView.as_view(), name="home-api")
]
