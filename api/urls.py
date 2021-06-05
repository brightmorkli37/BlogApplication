from django.urls import path, include
from rest_framework import routers
from .views import BlogViewSet

router = routers.DefaultRouter()
router.register('blog_api', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]