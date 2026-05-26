#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Service

# Update Building Works service with new image
service = Service.objects.filter(name__icontains='Building').first()
if service:
    service.image_url = '/static/images/services/building_works_civil.jpeg'
    service.save()
    print(f"Updated {service.name}")
    print(f"New image URL: {service.image_url}")
else:
    print("Building Works service not found")
