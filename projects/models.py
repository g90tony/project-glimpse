from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Models):
    display_picture = CloudinaryField('image', default=None)
    user_bio = models.TextField()
    user_mail = models.EmailField()


class Project(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=255)
    landing_page = CloudinaryField('image', default=None)
    detailed_description = models.TextField()
    link = models.CharField()
