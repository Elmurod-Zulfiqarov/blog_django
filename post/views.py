from django.shortcuts import render
from .models import Post, Contact, Tag, Category
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, ContactSerializer, TagSerializer, CategorySerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from helpers.pagination import CustomPagination

class HomeTemplateView(View):
	def get(self, request, *args, **kwargs):
		search = request.GET.get("search")
		print(search)			
		if search is None:
			post = Post.objects.all()[:12]
		else:
			post = Post.objects.filter(title__contains=search)
		return render(request, "post/index.html", {"post": post, "search": search})
	
		
class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	pagination_class = CustomPagination


class TopPostListView(ListAPIView):
	queryset = Post.objects.filter(is_popular=True)
	serializer_class = PostSerializer


class ResentlyPostListView(ListAPIView):
	queryset = Post.objects.order_by("-published_date")
	serializer_class = PostSerializer


class FeaturePostListView(ListAPIView):
	queryset = Post.objects.filter(is_feature=True)
	serializer_class = PostSerializer


class ContactCreateView(CreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer


class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class TagListView(ListAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

