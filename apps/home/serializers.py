from rest_framework import serializers
from apps.home.models import (
    HomeTitle,
    Banner,
    OurSuccess,
    LatestNews,
    HowItWorks,
    NeedSupport,
)

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'title', 'description']

class HomeTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTitle
        fields = ['id', 'title']

class OurSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurSuccess
        fields = ['id', 'title', 'description']

class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = ['id', 'title', 'description', 'images']

class HowItWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItWorks
        fields = ['id', 'title', 'description','icon']

class NeedSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedSupport
        fields = ['id','name','phone','email','yourQuery']
