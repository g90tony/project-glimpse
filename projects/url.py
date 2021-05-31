from django.urls import path


from .import views

app_name = 'projects'

urlpatterns = [
    path(r'^api/projects/list/all$', views.index.as_view()),
    path(r'^api/projects/view/(?P<project_id>[0-9])$', views.view_project.as_view()),
    path(r'^api/profile/)$', views.user_profile.as_view()),
    path(r'^api/profile/view/(?P<profile_id>[0-9])$', views.view_profile.as_view()),
]