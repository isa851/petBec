from django.contrib import admin
from apps.home.models import HomeTitle, HowItWorks, LatestNews, NeedSupport, OurSuccess

@admin.register(HomeTitle)
class HomeTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(HowItWorks)
class HowItWorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(NeedSupport)
class NeedSupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'yourQuery')

@admin.register(OurSuccess)
class OurSuccessAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')