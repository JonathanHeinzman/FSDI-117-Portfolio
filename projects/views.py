from django.shortcuts import render
from .models import Project, Skill

# Create your views here.
def projects_list(request):
    projects_list = Project.objects.all().order_by('-year')
    context = {'projects_list': projects_list}
    return render(request, 'projects/projects.html', context)