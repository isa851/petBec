from django.contrib import admin

from .models import Gallery, GalleryTitle

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(GalleryTitle)
class GalleryTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
