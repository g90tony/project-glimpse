from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from .import views

app_name = 'projects'

urlpatterns = [
    path('api/project/', views.ListProjects.as_view()),
    path('api/project/<int:project_id>', views.SingleProject.as_view()),
    
    path('api/profile/<int:user_id>', views.SingleProfile.as_view()),
  
    path('', views.index, name='Home'),
    path('profile/', views.profile, name='Profile'),  
    path('profile/create', views.create_profile, name='Create Profile'),
    
    path('project/new', views.upload, name='New Project'),  
    path('project/view', views.view, name='View Project'),  
]