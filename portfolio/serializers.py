from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Projects

class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields='__all__'