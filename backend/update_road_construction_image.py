#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Service

# Update Road Construction service with the new image
service = Service.objects.filter(name__icontains='Road Construction').first()
if service:
    service.image_url = '/static/images/services/road_construction_RIC7726.jpg'
    service.save()
    print(f"Updated {service.name}")
    print(f"New image URL: {service.image_url}")
else:
    print("Road Construction service not found")
