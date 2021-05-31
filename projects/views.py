from os import stat
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Project

from .serializer import ProjectSerializer, ProfileSerialier
from projects import serializer 
# Create your views here.
class ProjectsAPI(APIView):
    def project_getter(self, id):
        try:
            return Project.object.filter(id = id).first()
        
        except: 
            return Http404
        
    def get_project(self, project_id, request,format=None):
        project = self.project_getter(project_id)
        serializers = ProjectSerializer(project)
        
        return Response(serializer.data)
    
    
    def get_all_projects(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        
        return Response(serializers.data)
    
    
    def create_new_project(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
         
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update_existing_project(self, request, project_id, format=None):
        fetched_project = self.project_getter(project_id)
        serializers= ProjectSerializer(fetched_project, request.data)
        
        if serializer.is_valid():
            serializers.save()
            
            return Response(serializers.data)
        
        else: 
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete_existing_project(self, request, project_id, format=None):
        project = self.project_getter(project_id)
        project.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
class ProfileAPI(APIView):
    def profile_getter(self, id):
        try:
            return Profile.objects.filter(user=id).first()
        
        except Profile.DoesNotExist:
                return Http404
            
        
    def get_profile(self, request, profile_id, format=None): 
        profile = self.profile_getter(profile_id)
        serializers = ProfileSerialier(profile)
        
        return Response(serializers.data)
        
        
    def create_new_profile(self, request, format=None):
        serializers = ProfileSerialier(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update_profile(self, request, profile_id, format=None):
        fetched_profile = self.profile_getter(profile_id)
        serializers = ProfileSerialier(fetched_profile, request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data)
        
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    
    def delete_profile(self, request, profile_id, format=None):
        profile = self.profile_getter(profile_id)
        profile.delete()
        
        return Response(status= status.HTTP_204_NO_CONTENT)