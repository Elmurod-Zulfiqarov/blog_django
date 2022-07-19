from django.shortcuts import render
from .models import Post, Contact
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, ContactSerializer
from rest_framework.generics import CreateAPIView

class Home(View):
	def get(self, request, *args, **kwargs):
		search = request.GET.get("search")
		print(search)			
		if search is None:
			post = Post.objects.all()[:12]
		else:
			post = Post.objects.filter(title__contains=search)
		return render(request, "post/index.html", {"post": post, "search": search})
	
		
class Home_Drf(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	# search_fields = ["title", "tag", "category", "author"]


class ContactCreateView(CreateAPIView):
	queryset = Contact
	serializer_class = ContactSerializer
