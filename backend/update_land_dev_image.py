#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Service

# Update Land Development service with the new image
service = Service.objects.filter(name__icontains='Land Development').first()
if service:
    service.image_url = '/static/images/services/land_development_RIC7681.jpg'
    service.save()
    print(f"Updated {service.name}")
    print(f"New image URL: {service.image_url}")
else:
    print("Land Development service not found")
