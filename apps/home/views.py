from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.home.models import (
    Banner,
    HomeTitle,
    OurSuccess,
    LatestNews,
    HowItWorks,
    NeedSupport,
)
from apps.home.serializers import (
    BannerSerializer,
    HomeTitleSerializer,
    OurSuccessSerializer,
    LatestNewsSerializer,
    HowItWorksSerializer,
    NeedSupportSerializer,
)


class BannerViewSet(ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class HomeTitleViewSet(ModelViewSet):
    queryset = HomeTitle.objects.all()
    serializer_class = HomeTitleSerializer

class OurSuccessViewSet(ModelViewSet):
    queryset = OurSuccess.objects.all()
    serializer_class = OurSuccessSerializer

class LatestNewsViewSet(ModelViewSet):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializer

class HowItWorksViewSet(ModelViewSet):
    queryset = HowItWorks.objects.all()
    serializer_class = HowItWorksSerializer

class NeedSupportViewSet(CreateModelMixin, GenericViewSet):
    queryset = NeedSupport.objects.all()
    serializer_class = NeedSupportSerializer