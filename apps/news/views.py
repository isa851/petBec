from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(ModelViewSet):

    queryset = News.objects.all().order_by("-created_at")
    serializer_class = NewsSerializer