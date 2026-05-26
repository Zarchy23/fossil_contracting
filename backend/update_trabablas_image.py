#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Project

# Update Trabablas Interchange project with the new image
project = Project.objects.filter(name__icontains='Trabablas').first()
if project:
    project.image_url = '/static/images/trabablas-interchange/DJI_20250529171000_0065_D.jpg'
    project.save()
    print(f"Updated {project.name}")
    print(f"New image URL: {project.image_url}")
else:
    print("Trabablas project not found")
