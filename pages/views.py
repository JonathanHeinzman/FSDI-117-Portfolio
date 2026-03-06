from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def projects_view(request):
    return render(request, 'projects/projects.html')

def contact_me_view(request):
    return render(request, 'pages/contact_me.html')