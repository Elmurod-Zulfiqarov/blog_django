from django.urls import path
from .views import AuthorDetailView, AuthorListView, AuthorPostsView


urlpatterns = [
    path("author/", AuthorListView.as_view(), name='author'),
    path('author/<int:id>/', AuthorDetailView.as_view()),
    path('author/<int:author_id>/posts/', AuthorPostsView.as_view()),
]
