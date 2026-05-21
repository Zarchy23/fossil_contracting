#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Service

services_data = [
    {
        'name': 'Road Construction',
        'description': 'We specialize in flexible pavement design and construction, full road rehabilitation, comprehensive drainage systems, and premium asphalt surfacing.',
        'icon': 'fas fa-road',
        'image_url': '/static/images/DJI_20250530162006_0002_V.jpg',
        'order': 1,
        'is_featured': True
    },
    {
        'name': 'Land Development',
        'description': 'Comprehensive land development services including site planning, land clearing, grading, and infrastructure preparation for residential and commercial projects.',
        'icon': 'fas fa-map',
        'image_url': '/static/images/land-development.jpg',
        'order': 2,
        'is_featured': True
    },
    {
        'name': 'Earth Works',
        'description': 'Bulk earthmoving operations, precision excavations, strategic stockpiling, and efficient load & haul services for large-scale projects.',
        'icon': 'fas fa-mountain',
        'image_url': '/static/images/DJI_20250530162737_0039_V.jpg',
        'order': 3,
        'is_featured': True
    },
    {
        'name': 'Building Works',
        'description': 'Complex residential and industrial construction projects delivered to international standards with complete project management.',
        'icon': 'fas fa-building',
        'image_url': '/static/images/DJI_20250529171556_0077_D.jpg',
        'order': 4,
        'is_featured': True
    },
    {
        'name': 'Contract Mining',
        'description': 'Opencast chrome and coal mining operations with modern equipment fleet, full rehabilitation, and environmental compliance.',
        'icon': 'fas fa-hammer',
        'image_url': '/static/images/DJI_20250529171427_0071_D.jpg',
        'order': 5,
        'is_featured': False
    },
    {
        'name': 'Plant Hire',
        'description': 'Complete fleet of heavy machinery and equipment available for hire, including dozers, excavators, and specialized mining equipment.',
        'icon': 'fas fa-wrench',
        'image_url': '/static/images/DJI_20250529171044_0066_D.jpg',
        'order': 6,
        'is_featured': False
    },
    {
        'name': 'Water Infrastructure',
        'description': 'Dam construction, water supply systems, and irrigation infrastructure projects with environmental sustainability measures.',
        'icon': 'fas fa-water',
        'image_url': '/static/images/DJI_20250529171000_0065_D.jpg',
        'order': 7,
        'is_featured': False
    }
]

# Clear existing services
Service.objects.all().delete()
print(f'Cleared existing services')

# Create new services
for service_data in services_data:
    service = Service.objects.create(**service_data)
    print(f'✓ Created: {service.name}')

print(f'\n✓ Total services created: {Service.objects.count()}')
