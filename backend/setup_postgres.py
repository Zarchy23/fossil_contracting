#!/usr/bin/env python
"""
PostgreSQL Setup Script
Creates database and user for Fossil Contracting
"""

import subprocess
import sys

print("""
╔════════════════════════════════════════════════════════════════╗
║         PostgreSQL Database Setup                              ║
╚════════════════════════════════════════════════════════════════╝
""")

# Commands to run in PostgreSQL
postgres_commands = [
    # Create database
    "CREATE DATABASE fossil_contracting;",
    # List databases to verify
    "\\l",
    # Show current user
    "\\du"
]

print("Running PostgreSQL setup commands...")
print("\nPlease enter when prompted for PostgreSQL password (leave blank if none):")
print("Commands to execute:")
for cmd in postgres_commands:
    print(f"  > {cmd}")

try:
    # Connect to PostgreSQL and run commands
    psql_cmd = 'psql -U postgres -c "CREATE DATABASE IF NOT EXISTS fossil_contracting;"'
    result = subprocess.run(
        psql_cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("\n✓ Database setup completed successfully!")
        print("\nNext steps:")
        print("  1. Update .env file if needed")
        print("  2. Run: cd backend && python manage.py migrate")
        print("  3. Run: python manage.py runserver")
    else:
        print("\n✗ Error during setup:")
        print(result.stderr)
        print("\nManual setup instructions:")
        print("  1. Open PowerShell as Administrator")
        print("  2. Run: psql -U postgres")
        print("  3. In psql prompt, run:")
        print("     CREATE DATABASE fossil_contracting;")
        print("     \\q")
        
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nPlease run these commands manually in PostgreSQL:")
    print("  psql -U postgres")
    print("  CREATE DATABASE fossil_contracting;")
    print("  \\q")
