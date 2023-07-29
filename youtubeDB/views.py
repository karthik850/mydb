from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyYotubeVideos, SubscriberStories, YoutubeEvents
from .serializers import MYYoutubeEventsSerializer, MyYoutubeVideosSerializers, SubscriberStoriesSerializer

# Create your views here.

class myYoutubeViews(APIView):
    def get(self,request):
        videos1=MyYotubeVideos.objects.all()
        serializer=MyYoutubeVideosSerializers(videos1,many=True)
        return Response(serializer.data)

class subscriberStoryViews(APIView):
    def post(self,request):
        serializer = SubscriberStoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class myYoutubeEvents(APIView):
    def get(self,request):
        events=YoutubeEvents.objects.all()
        serializer=MYYoutubeEventsSerializer(events,many=True)
        return Response(serializer.data)

