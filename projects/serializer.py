from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Profile, Project

class UserSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email",)
        
class ProfileSerialier(serializers.ModelSerializer):
    user = UserSerialier(many=False)
    display_picture = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ("id","display_picture", "user_bio", "user_mail", "user")
        
    def get_display_picture(self, profile):
        request = self.context.get('request')
        display_picture = profile.display_picture.url
        return request.build_absolute_uri(display_picture)

class ProjectSerializer(serializers.ModelSerializer):
    profile = ProfileSerialier(many=False)
    landing_page = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields =("id","profile", "title", "landing_page", "detailed_description", "link",)
        
    def get_landing_page(self, project):
        request = self.context.get('request')
        landing_page = project.landing_page.url
        return request.build_absolute_uri(landing_page)

class ProjectsSerializer(serializers.ModelSerializer):
    profile = ProfileSerialier(many=False)
    landing_page = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields =("profile", "title", "landing_page", "detailed_description", "link",)
        
    def get_landing_page(self, project):
        request = self.context.get('request')
        landing_page = project.landing_page.url
        return request.build_absolute_uri(landing_page)