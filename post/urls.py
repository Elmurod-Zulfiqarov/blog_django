from django.urls import path, include

from .views import (
	HomeTemplateView, PostViewSet, 
	ContactCreateView, PostListView, 
	CategoryListView, TagListView,
	TopPostListView, ResentlyPostListView, FeaturePostListView
)
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register("post", PostViewSet, basename="home-drf")

urlpatterns = [
	path("", HomeTemplateView.as_view(), name="home"),
	# path("api/v1/", include(router.urls)), # modelViewSet ishlamasa  pastdagilar ishlaydi
	path("api/v1/contact/", ContactCreateView.as_view(), name="contact"),
	path("api/v1/post/", PostListView.as_view(), name="post"),
	path("api/v1/post/top/", TopPostListView.as_view(), name="post_top"),
	path("api/v1/post/resently/", ResentlyPostListView.as_view(), name="post_resently"),
	path("api/v1/post/featured/", FeaturePostListView.as_view(), name="post_feature"),
	path("api/v1/category/", CategoryListView.as_view(), name="category"),
	path("api/v1/tag/", TagListView.as_view(), name="tag")	
]
