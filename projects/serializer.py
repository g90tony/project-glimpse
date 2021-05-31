from django.db.models import fields
from rest_framework import serializers
from .models import Profile, Project

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =("profile", "title", "landing_page", "detailed_description", "link",)
        
class ProfileSerialier(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("display_picture", "user_bio", "user_mail", )