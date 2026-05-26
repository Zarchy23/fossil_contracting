#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Service

# Update Earth Works service with new image
service = Service.objects.filter(name__icontains='Earth').first()
if service:
    service.image_url = '/static/images/services/earth_works_RIC1733.jpg'
    service.save()
    print(f"Updated {service.name}")
    print(f"New image URL: {service.image_url}")
else:
    print("Earth Works service not found")
