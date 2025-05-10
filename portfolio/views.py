import json
import os
from django.shortcuts import render
from django.conf import settings

def home(request):
    json_path = os.path.join(settings.BASE_DIR, 'portfolio', 'projects.json')
    with open(json_path, 'r') as f:
        projects = json.load(f)
    return render(request, 'portfolio/home.html', {'projects': projects})

def new_page_view(request):
    return render(request, 'bio.html')

