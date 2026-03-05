from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.home.views import (
    BannerViewSet,
    HomeTitleViewSet,
    OurSuccessViewSet,
    LatestNewsViewSet,
    HowItWorksViewSet,
    NeedSupportViewSet,
)

router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'home-title', HomeTitleViewSet, basename='home-title')
router.register(r'our-success', OurSuccessViewSet, basename='our-success')
router.register(r'latest-news', LatestNewsViewSet, basename='latest-news')
router.register(r'how-it-works', HowItWorksViewSet, basename='how-it-works')
router.register(r'need-support', NeedSupportViewSet, basename='need-support')

urlpatterns = [
    path('', include(router.urls)),
]
