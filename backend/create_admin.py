#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

from django.contrib.auth.models import User

# Check if admin user exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@fossilzim.com', 'admin123')
    print("✓ Admin user created successfully!")
    print("  Username: admin")
    print("  Email: admin@fossilzim.com")
    print("  Password: admin123")
else:
    print("✓ Admin user already exists")
    print("  You can change the password using: python manage.py changepassword admin")
