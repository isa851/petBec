from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.news.views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]