from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import MileStones, MyYotubeVideos,SubscriberStories, YoutubeEvents

class MyYoutubeVideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyYotubeVideos
        fields='__all__'

class SubscriberStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberStories
        fields='__all__'

class MYYoutubeEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeEvents
        fields='__all__'

        
class MyYoutubeMilestonesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MileStones
        fields='__all__'