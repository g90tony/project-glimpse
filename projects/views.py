from os import stat
from django.http.response import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile, Project
from .forms import NewProfile, NewProject
from .serializer import ProjectSerializer, ProjectsSerializer, ProfileSerialier
from .permissions import IsAdminOrReadOnly 
# Create your views here.
class ListProjects(APIView):
    
    # permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
    
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingleProject(APIView):
    permission_classes = (IsAdminOrReadOnly)
      
    def project_getter(self, id):
        try:
            return Project.object.filter(id = id).first()
        
        except: 
            return Http404
        
    def get(self, project_id, request,format=None):
        project = self.project_getter(project_id)
        serializers = ProjectSerializer(project)
        
        return Response(serializers.data)
    
    
    def update(self, request, project_id, format=None):
        fetched_project = self.project_getter(project_id)
        serializers= ProjectSerializer(fetched_project, request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data)
        
        else: 
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, project_id, format=None):
        project = self.project_getter(project_id)
        project.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class SingleProfile(APIView):
    def profile_getter(self, id):
        try:
            return Profile.objects.filter(user=id).first()
        
        except Profile.DoesNotExist:
                return Http404
            
        
    def get(self, request, profile_id, format=None): 
        profile = self.profile_getter(profile_id)
        serializers = ProfileSerialier(profile)
        
        return Response(serializers.data)
        
        
    def post(self, request, format=None):
        serializers = ProfileSerialier(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, profile_id, format=None):
        fetched_profile = self.profile_getter(profile_id)
        serializers = ProfileSerialier(fetched_profile, request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data)
        
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    
    def delete(self, request, profile_id, format=None):
        profile = self.profile_getter(profile_id)
        profile.delete()
        
        return Response(status= status.HTTP_204_NO_CONTENT)
    
@login_required(login_url='accounts/login/')  
def index(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    
    if current_user is None:
        return redirect('/profile/create')
    
    all_projects = Project.objects.all()
    title = 'Profile Glimpse: Home'
    
    return render(request, 'index.html', {'title': title, 'projects': all_projects})


@login_required(login_url='accounts/login/')
def profile(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    user_projects = Project.objects.filter(profile = current_user).all()
    title = f'Project Glimpse: Profile'
    
    
    return render(request, 'profile.html', {'title': title,'profile': current_user, 'posts': user_projects})

@login_required(login_url='accounts/login/')
def create_profile(request):
    
    title = 'Profile Glimpse: Create Profile'
    
    if request.method == 'POST':
    
        current_user = request.user
        
        display_picture = request.POST.get('display_picture')
        user_bio = request.POST.get('user_bio')
        
        user_mail = request.user.email
        
        new_profile = Profile(display_picture= display_picture, user_bio= user_bio, user_mail = user_mail, user = current_user)
        new_profile.save()

        data = {'success': 'Your profile was created successfully. '}
        return JsonResponse(data)
    
    else:
        return render(request, 'profile_create.html', {'title': title})
    
@login_required(login_url='accounts/login/')
def view(request, project_id):
    
    project = Project.objects.filter(id = project_id).first()
    title = 'Project GlimpseL: View Project'
    
    return render(request, 'view.html', {'title': title, 'project': project })



@login_required(login_url='accounts/login/')
def upload(request):
    title = 'Project Glimpse: New Post'
    current_user = Profile.objects.filter(user = request.user).first()
    
    return render(request, 'create.html', {"title": title, "profile": current_user})



@login_required(login_url='accounts/login/')
def new_profile(request):
    title = 'Project Glimpse: Create Profile'
    
    if request.method == 'POST':
        form = NewProfile(request.POST, request.FILES)
        
        if form.is_valid():
            new_profile = form.save(commit = False)
            new_profile.user = request.user
            
            new_profile.save()
            
            return redirect('/')
        
    else:
        form = NewProject()
        
    return render(request, 'profile_init.html', {"title": title, 'form': form})
        
        
            
            