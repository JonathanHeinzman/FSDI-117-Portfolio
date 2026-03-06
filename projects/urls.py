from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.projects_list, name='projects_list'),
]