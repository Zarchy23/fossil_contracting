#!/usr/bin/env python
"""
Quick run script for Django development server
Run from project root: python run.py
"""
import os
import subprocess
import sys

# Change to backend directory
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
os.chdir(backend_dir)

# Run manage.py runserver with any passed arguments
cmd = [sys.executable, 'manage.py', 'runserver'] + sys.argv[1:]
subprocess.run(cmd)
