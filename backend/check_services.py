#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Service

services = Service.objects.all()[:4]
for s in services:
    print(f'\n{"="*60}')
    print(f'Name: {s.name}')
    desc = s.description[:100] + '...' if len(s.description) > 100 else s.description
    print(f'Description: {desc}')
    print(f'Icon: {s.icon}')
    print(f'Image URL: {s.image_url}')
    print(f'Order: {s.order}')
