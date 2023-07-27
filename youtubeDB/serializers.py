from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import MyYotubeVideos

class MyYoutubeVideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyYotubeVideos
        fields='__all__'