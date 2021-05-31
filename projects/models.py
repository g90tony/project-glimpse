from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    display_picture = CloudinaryField('image', default=None)
    user_bio = models.TextField()
    user_mail = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    landing_page = CloudinaryField('image', default=None)
    detailed_description = models.TextField()
    link = models.CharField(max_length=225)
