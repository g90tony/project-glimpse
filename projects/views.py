from os import stat
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Project

from .serializer import ProjectSerializer, ProfileSerialier 
# Create your views here.
class ProjectsAPI(APIView):
    def get_all_projects(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        
        return Response(serializers.data)
    
    def create_new_project(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileAPI(APIView):
    def get_profile(self, request, format=None):
        found_profile =  Profile.objects.filter(request.user_id).first()
        serializers = ProfileSerialier(found_profile, many=False)
        if serializers.is_valid():
            return Response(serializers.data, status=status.HTTP_200_OK)

        else:
            return Response(serializers.data, status=status.HTTP_404_NOT_FOUND)
        
    def create_new_profile(self, request, format=None):
        serializers = ProfileSerialier(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
        
        