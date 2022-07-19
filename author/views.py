from rest_framework.generics import RetrieveAPIView, ListAPIView
from helpers.pagination import CustomPagination
from post.models import Post
from post.serializers import PostSerializer
from .models import Author
from .serializers import AuthorSerializer


class AuthorListView(ListAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class AuthorDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'


class AuthorPostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('author_id', None):
            queryset = queryset.filter(author__id=self.kwargs['author_id'])

        return queryset