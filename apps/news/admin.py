from django.contrib import admin
from apps.news.models import News, NewsTitle



@admin.register(NewsTitle)
class NewsTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'