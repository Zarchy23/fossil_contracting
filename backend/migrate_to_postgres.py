#!/usr/bin/env python
"""
PostgreSQL Migration Guide
This script helps migrate from SQLite to PostgreSQL
"""

import os
import sys
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossil_backend.settings')
django.setup()

print("""
╔════════════════════════════════════════════════════════════════╗
║         PostgreSQL Migration Setup                             ║
╚════════════════════════════════════════════════════════════════╝

STEP 1: PostgreSQL Installation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before proceeding, ensure PostgreSQL is installed:

Windows:
  1. Download from https://www.postgresql.org/download/windows/
  2. Run installer (use default settings)
  3. Remember the password for the 'postgres' user

After installation, verify PostgreSQL is running:
  psql --version

STEP 2: Create PostgreSQL Database
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run these commands in PowerShell as Administrator:

  # Connect to PostgreSQL
  psql -U postgres

  # In the psql prompt, run:
  CREATE DATABASE fossil_contracting;
  \\q  (to exit)

STEP 3: Update Environment Variables
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Edit the .env file and update if needed:
  DB_NAME=fossil_contracting
  DB_USER=postgres
  DB_PASSWORD=<your-postgres-password>
  DB_HOST=localhost
  DB_PORT=5432

STEP 4: Run Migrations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  cd backend
  python manage.py migrate

STEP 5: Restore Data (Optional)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If you want to restore your data from SQLite:
  python populate_projects.py
  python populate_services.py
  python create_admin.py

STEP 6: Test the Setup
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  python manage.py runserver

Your backup SQLite database is saved as:
  backend/db.sqlite3.backup.20260522_110207

🎉 Migration Complete!
""")

# Check current database configuration
from django.db import connection
print("\nCurrent Database Configuration:")
print(f"  Engine: {connection.settings_dict['ENGINE']}")
print(f"  Database: {connection.settings_dict.get('NAME', 'N/A')}")
print(f"  Host: {connection.settings_dict.get('HOST', 'N/A')}")
print(f"  Port: {connection.settings_dict.get('PORT', 'N/A')}")
