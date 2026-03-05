from rest_framework.viewsets import ModelViewSet
from .models import Gallery
from .serializers import GallerySerializer
from core.pagination import GalleryPagination


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = GalleryPagination