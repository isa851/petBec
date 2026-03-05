from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # API
    path("api/v1/home/", include("apps.home.urls")),
    path("api/v1/news/", include("apps.news.urls")),
    path("api/v1/gallery/", include("apps.gallery.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)