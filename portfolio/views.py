from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Projects
from .serializers import ProjectsSerializers

# Create your views here.

class projectView(APIView):
    def get(self,request):
        projects1=Projects.objects.all()
        serializer=ProjectsSerializers(projects1,many=True)
        return Response(serializer.data)


