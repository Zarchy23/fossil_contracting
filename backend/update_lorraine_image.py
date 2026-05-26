#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Project

# Update Lorraine Drive project with the new image
project = Project.objects.filter(name__icontains='Lorraine').first()
if project:
    project.image_url = '/static/images/lorraine-drive/_RIC1821.jpg'
    project.save()
    print(f"Updated {project.name}")
    print(f"New image URL: {project.image_url}")
else:
    print("Lorraine Drive project not found")
