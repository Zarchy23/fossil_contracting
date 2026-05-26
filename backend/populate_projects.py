#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from api.models import Project
from datetime import datetime, timedelta

projects_data = [
    {
        'name': 'Harare-Chirundu Highway',
        'location': 'Harare to Chirundu, Zimbabwe',
        'value_usd': 365000000.00,
        'completion_percentage': 100,
        'client': 'Ministry of Transport',
        'description': 'The Harare–Chirundu Road Rehabilitation Project is one of Zimbabwe\'s major national infrastructure developments aimed at improving transportation efficiency, road safety, and regional trade connectivity.',
        'status': 'COMPLETED',
        'image_url': '/static/images/harare-chirundu/Fossil-2.jpg',
        'is_featured': True,
        'start_date': datetime(2024, 1, 1).date(),
        'end_date': datetime(2025, 12, 31).date()
    },
    {
        'name': 'Lorraine Drive Road',
        'location': 'Lorraine Drive, Harare, Zimbabwe',
        'value_usd': 5000000.00,
        'completion_percentage': 100,
        'client': 'Harare City Council',
        'description': 'Urban road rehabilitation project focused on upgrading and rehabilitating the road through asphalt surfacing, drainage improvements, and earthworks.',
        'status': 'COMPLETED',
        'image_url': '/static/images/lorraine-drive/_RIC7669.jpg',
        'is_featured': True,
        'start_date': datetime(2024, 6, 1).date(),
        'end_date': datetime(2025, 12, 31).date()
    },
    {
        'name': 'Trabablas Interchange',
        'location': 'Trabablas, Harare, Zimbabwe',
        'value_usd': 45000000.00,
        'completion_percentage': 85,
        'client': 'Ministry of Transport',
        'description': 'Major road interchange development project involving complex earthworks, drainage systems, road construction, and traffic management infrastructure.',
        'status': 'ONGOING',
        'image_url': '/static/images/trabablas-interchange/DJI_20250204144414_0057_V.JPG',
        'is_featured': True,
        'start_date': datetime(2024, 3, 1).date(),
        'end_date': None
    },
    {
        'name': 'Harare-Beitbridge Road',
        'location': 'Harare to Beitbridge, Zimbabwe',
        'value_usd': 200000000.00,
        'completion_percentage': 60,
        'client': 'Ministry of Transport',
        'description': 'Major highway rehabilitation project connecting Zimbabwe to South Africa, involving extensive road reconstruction, widening, and modernization.',
        'status': 'ONGOING',
        'image_url': '/static/images/DJI_20250530162006_0002_V.jpg',
        'is_featured': False,
        'start_date': datetime(2024, 9, 1).date(),
        'end_date': None
    }
]

# Clear existing projects (optional - uncomment if you want to reset)
# Project.objects.all().delete()
# print('Cleared existing projects')

# Create or update projects
for project_data in projects_data:
    project, created = Project.objects.update_or_create(
        name=project_data['name'],
        defaults=project_data
    )
    action = 'Created' if created else 'Updated'
    print(f'✓ {action}: {project.name}')

print(f'\n✓ Total projects: {Project.objects.count()}')
