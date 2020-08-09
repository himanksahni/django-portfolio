from django.shortcuts import render, get_object_or_404
from .models import Projects

def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {'projects': projects})

def project(request, project_id):
    print(project_id)
    project = get_object_or_404(Projects, pk= project_id)
    return render(request, 'projects/home.html', {'project': project})
