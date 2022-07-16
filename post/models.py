from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
	name = models.CharField(max_length=128)


class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	decription = models.TextField(max_length=1024)
	image = models.ImageField()
	date_createted = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now_add=True)
	total_views = models.PositiveIntegerField()

