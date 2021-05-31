from os import stat
from django.http.response import Http404
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
    def profile_getter(self, user_id):
        try:
            return Profile.objects.filter(user=user_id).first()
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        except Profile.DoesNotExist:
                return Http404
            
        
    def get_profile(self, request, user_id, format=None): 
        profile = self.profile_getter(user_id)
        serializers = ProfileSerialier(profile)
        
        return Response(serializers.data)
        
    def create_new_profile(self, request, format=None):
        serializers = ProfileSerialier(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
        
        