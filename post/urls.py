from django.urls import path, include

from post.models import Contact
from .views import Home, Home_Drf, ContactCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("post", Home_Drf, basename="home-drf")

urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("api/v1/", include(router.urls)),
	path("api/v1/contact/", ContactCreateView.as_view(), name="contact")
]
