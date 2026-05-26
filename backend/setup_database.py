#!/usr/bin/env python
"""
PostgreSQL Setup - Creates database and user for Fossil Contracting
Run with: python setup_database.py
"""

import subprocess
import sys
import os

print("""
╔════════════════════════════════════════════════════════════════╗
║         PostgreSQL Database & User Setup                       ║
║         Fossil Contracting                                     ║
╚════════════════════════════════════════════════════════════════╝
""")

# SQL setup script path
sql_file = os.path.join(os.path.dirname(__file__), 'setup_fossil_db.sql')

print("\nStep 1: Running PostgreSQL Setup")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

try:
    # Run the SQL setup file
    cmd = f'psql -U postgres -f "{sql_file}"'
    print(f"Executing: {cmd}\n")
    
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✓ PostgreSQL setup successful!")
        print("\nOutput:")
        print(result.stdout)
        
        print("\n" + "="*60)
        print("Step 2: Next Actions")
        print("="*60)
        print("""
Your PostgreSQL setup is complete:
  ✓ fossil_user role created (password: fossil_password)
  ✓ fossil_contracting database created
  ✓ Permissions granted

Now run these commands to finalize:
  
  1. Install/upgrade Python packages:
     pip install -r requirements.txt
  
  2. Run Django migrations:
     python manage.py migrate
  
  3. Populate initial data (optional):
     python populate_projects.py
     python populate_services.py
     python create_admin.py
  
  4. Start the server:
     python manage.py runserver

Your SQLite backup is safe at:
  backend/db.sqlite3.backup.20260522_110207
""")
        
    else:
        print("✗ Setup encountered an error:")
        print(result.stderr)
        print("\nDEBUG INFO:")
        print(result.stdout)
        print("\nTroubleshooting:")
        print("  1. Ensure PostgreSQL is running")
        print("  2. Open PowerShell as Administrator")
        print("  3. Try running the SQL commands manually:")
        print(f"     psql -U postgres -f \"{sql_file}\"")
        sys.exit(1)
        
except FileNotFoundError:
    print("✗ PostgreSQL command 'psql' not found!")
    print("\nPlease:")
    print("  1. Install PostgreSQL from https://www.postgresql.org/download/windows/")
    print("  2. Add PostgreSQL bin folder to PATH")
    print("  3. Restart your terminal")
    print("  4. Run this script again")
    sys.exit(1)
    
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    sys.exit(1)
