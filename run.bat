@echo off
REM Start Django development server from project root
cd backend
python manage.py runserver %*
pause
