from rest_framework.serializers import ModelSerializer
from author.models import Author, AuthorJob


class AuthorJobSerializer(ModelSerializer):
	class Meta:
		model = AuthorJob
		fields = '__all__'


class AuthorSerializer(ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'
		depth = 1
