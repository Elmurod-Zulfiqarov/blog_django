from django.db import models
from helpers.models import BaseModel
from manager.models import TopAuhtorManager


class AuthorJob(BaseModel):
	title = models.CharField(max_length=128)


class Author(BaseModel):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	avatar = models.ImageField(upload_to="avtor/", null=True)

	jobs = models.ManyToManyField(AuthorJob)
	bio = models.TextField()
	work_place = models.CharField(max_length=128,null=True)
	
	instagram_link = models.CharField(max_length=128)
	facebook_link = models.CharField(max_length=128)
	twitter_link = models.CharField(max_length=128)
	pinterest_link = models.CharField(max_length=128)

	posts_count = models.IntegerField(default=0)
	is_top = models.BooleanField(default=False)
	# top_authors = TopAuhtorManager()
