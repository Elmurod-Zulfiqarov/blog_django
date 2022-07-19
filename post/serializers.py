from rest_framework.serializers import ModelSerializer
from post.models import Post, Category, Tag, Contact


class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class TagSerializer(ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'

	
class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
		depth = 1


class ContactSerializer(ModelSerializer):
	class Meta:
		model = Contact
		fields = "__all__"
		