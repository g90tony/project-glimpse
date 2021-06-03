from django.db.models import fields
from rest_framework import serializers
from .models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =("id","profile", "title", "landing_page", "detailed_description", "link",)

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =("profile", "title", "landing_page", "detailed_description", "link",)
        
class ProfileSerialier(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id","display_picture", "user_bio", "user_mail", )