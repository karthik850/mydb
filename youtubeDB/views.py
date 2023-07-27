from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyYotubeVideos
from .serializers import MyYoutubeVideosSerializers

# Create your views here.

class myYoutubeViews(APIView):
    def get(self,request):
        videos1=MyYotubeVideos.objects.all()
        serializer=MyYoutubeVideosSerializers(videos1,many=True)
        return Response(serializer.data)


